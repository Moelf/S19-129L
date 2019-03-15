import pickle
# read about the utility functions in ./ex2utils.py
from ex2utils import *

# A simulation to produce
# 1000 finals states of the following decay chain
# with no displacement considered
# http://pdg.lbl.gov/2017/reviews/rpp2017-rev-kinematics.pdf
# ---------------------------------------------------------
# B+ -> D*0 + pi+
#        |
#        ---> D0 + pi0
#             |     |
#             |     ---> gamma + gamma
#             ---> K- + pi+
# ---------------------------------------------------------

# mass constants in GeV
mB_p = 5.28
mD_star0 = 2.01
mD_0 = 1.86
mK_m = 0.494
mPi_p = 0.1396
mPi_0 = 0.1350


output = []
# ----------------------------------------------------------------------------
# 1. Make all decays in rest frame of parent particle, 3-momentums are trivial
# 2. In spin = 1 case, rotate daughter 4-momentum in their parent's theta
#    because decay(helicity) angle distribution was given in the rest frame of
#    parent particle (weird to think about
# 3. Boost each particle with its parent's beta, propagate till final state
#    to obtain what we shall measure in LAB frame
# 4. Profit
# ----------------------------------------------------------------------------

# for _ in tqdm(range(1000)):
for _ in range(1000):
    # B+ -> D*0 + pi+
    # LAB frame, no boost needed
    Dstar0, Pi_p1 = restDecay(mB_p, mD_star0, mPi_p, spin=0)
    # rotation information about D_star0 particle for the daughters
    axis = np.cross(Dstar0.get_r(), [0, 0, 1])
    # rotate daughters back by theta, thus the negative
    angle = Dstar0.theta()

    # decay from spin 1, first rotate then boost back to LAB
    # D*0 -> D0 + pi0
    D0, Pi0 = restDecay(mD_star0, mD_0, mPi_0, spin=1)
    # rotate daughters back by theta, thus the negative
    roteMatrix = D0.rotate_by_axis(axis, -angle)
    Pi0.rotate_by_matrix(roteMatrix)
    D0.boost(PtoV(Dstar0))
    Pi0.boost(PtoV(Dstar0))

    # repeat
    K_m, Pi_p2 = restDecay(mD_0, mK_m, mPi_p, spin=0)
    K_m.boost(PtoV(D0))
    Pi_p2.boost(PtoV(D0))

    # repeat
    Gamma1, Gamma2 = restDecay(mPi_0, 0, 0, spin=0)
    Gamma1.boost(PtoV(Pi0))
    Gamma2.boost(PtoV(Pi0))

    output.append([Pi_p1, K_m, Pi_p2, Gamma1, Gamma2])

with open('data.pik', 'wb') as File:
    pickle.dump(output, File)
