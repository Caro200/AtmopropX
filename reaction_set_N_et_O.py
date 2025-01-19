# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:41:30 2025

@author: liamg
"""

from scipy.constants import pi, e, k, epsilon_0 as eps_0, c, m_e

species_list = Species([Specie("e", m_e, -e), Specie("N_2", 4.65e-26, 0), Specie("N", 2.33e-26, 0), Specie("N_2+", 4.65e-26, e), Specie("N+", 2.33e-26, e), Specie("O_2+", 5.31e-26, e), Specie("O_2", 5.31e-26, 0), Specie("O", 2.67e-26, 0), Specie("O+", 2.67e-26, e)])

exc1_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc1_N2"), 6.17, [1., 1.])
exc2_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc2_N2"), 7.35, [1., 1.])
exc3_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc3_N2"), 7.36, [1., 1.])
exc4_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc4_N2"), 8.16, [1., 1.])
exc5_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc5_N2"), 8.40, [1., 1.])
exc6_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc6_N2"), 8.55, [1., 1.])
exc7_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc7_N2"), 8.89, [1., 1.])
exc8_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc8_N2"), 12.50, [1., 1.])
exc9_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc9_N2"), 12.90, [1., 1.])
exc10_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc10_N2"), 12.10, [1., 1.])
exc11_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc11_N2"), 12.90, [1., 1.])
exc12_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc12_N2"), 11.00, [1., 1.])
exc13_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc13_N2"), 11.90, [1., 1.])
exc14_N2 = Reaction(species_list, ["N2"], ["N2"], get_K_func(species_list, "N2", "exc14_N2"), 12.30, [1., 1.])
ion01_N2 = Reaction(species_list, ["N2"], ["e", "N2+"], get_K_func(species_list, "N2, N2+", "ion01_N2"), 15.60, [1., 1., 1.])
exc1_N = Reaction(species_list, ["N"], ["N"], get_K_func(species_list, "N", "exc1_N"), 3.20, [1., 1.])
exc2_N = Reaction(species_list, ["N"], ["N"], get_K_func(species_list, "N", "exc2_N"), 4.00, [1., 1.])
ion01_N = Reaction(species_list, ["N"], ["e", "N+"], get_K_func(species_list, "N", "ion01_N"), 14.80, [1., 1., 1.])
ela_N = ElasticCollisionWithElectron(species_list, ["N"], get_K_func(species_list, "N", "ela_N"), 0)
dion_N2 = Reaction(species_list, ["N2"], ["N", "N+", "e"], get_K_func(species_list, "N2", "dion_N2"), 18.00, [1., 1., 1., 1.])
ela_N2 = ElasticCollisionWithElectron(species_list, ["N2"], get_K_func(species_list, "N2", "ela_N2"), 0)

exc1_O2 = Reaction(species_list, ["O2"], ["O2"], get_K_func(species_list, "O2", "exc1_O2"), 1.00, [1., 1.])
exc2_O2 = Reaction(species_list, ["O2"], ["O2"], get_K_func(species_list, "O2", "exc2_O2"), 1.50, [1., 1.])
exc3_O2 = Reaction(species_list, ["O2"], ["O2"], get_K_func(species_list, "O2", "exc3_O2"), 4.50, [1., 1.])
exc4_O2 = Reaction(species_list, ["O2"], ["O2"], get_K_func(species_list, "O2", "exc4_O2"), 7.10, [1., 1.])
ion01_O2 = Reaction(species_list, ["O2"], ["e", "O2+"], get_K_func(species_list, "O2", "ion01_O2"), 12.10, [1., 1., 1.])
ela_O2 = ElasticCollisionWithElectron(species_list, ["O2"], get_K_func(species_list, "O2", "ela_O2"), 0)
diss1_O2 = Reaction(species_list, ["O2"], ["O"], get_K_func(species_list, "O2", "diss1_O2"), 6.12, [1., 2.])
diss2_O2 = Reaction(species_list, ["O2"], ["O"], get_K_func(species_list, "O2", "diss2_O2"), 8.40, [1., 2.])
exc1_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc1_O"), 1.97, [1., 1.])
exc2_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc2_O"), 4.19, [1., 1.])
exc3_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc3_O"), 9.52, [1., 1.])
exc4_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc4_O"), 12, [1., 1.])
exc5_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc5_O"), 12, [1., 1.])
exc6_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc6_O"), 12, [1., 1.])
exc7_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc7_O"), 12, [1., 1.])
exc8_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc8_O"), 12, [1., 1.])
exc9_O = Reaction(species_list, ["O"], ["O"], get_K_func(species_list, "O", "exc9_O"), 12, [1., 1.])
ela_O = ElastoicCollisionWithElectron(species_list, ["O"], get_K_func(species_list, "O", "ela_O"), 0)


