###############################################################################

#                 This program was produced by Trevor Thomas.                 #
#               Kick ass, go to space, represent the human race.              #

###############################################################################

"""
Orbit
=====

PURPOSE         :
-------
Equations for modelling Keplerian orbitals, primarily in Earth two body 
    systems. Equations are largely collected from Pritchard and Scuilli's
    Satellite Communications.

FIRST PRODUCED  :   2024/12/24 by Trevor Thomas

"""

###############################################################################
###                                 IMPORTS                                 ###
###############################################################################

from dataclasses import dataclass
from numpy import ndarray, power, square
from numpy.linalg import norm

from pint import Quantity

###############################################################################
###                                CONSTANTS                                ###
###############################################################################

GRAVITATIONAL_CONSTANT:Quantity|float = Quantity(
    6.6743e-11, 'N * m ** 2 / kg ** 2')

EARTH_ACCEL_CONSTANT:Quantity|float = Quantity(
    3.986018e5, 'km ** 3 / s ** 2')

###############################################################################
###                                GLOBALS                                  ###
###############################################################################



###############################################################################
###                            GLOBAL FUNCTIONS                             ###
###############################################################################

def calculate_gravitational_force(m_0:Quantity,
                                  m_1:Quantity,
                                  r:Quantity) -> Quantity:
    """
    Calculates the gravitational force between two bodies given their mass and
        separation.

    Parameters
    ----------
    m_0 : Quantity
        First mass.
    m_1 : Quantity
        Second mass.
    r : Quantity
        Seperation of center of masses.

    Returns
    -------
    Quantity
        The attractive gravitational force acting on the bodies.

    Notes
    -----
    Does not account for relativistic effects.
    """
    return -GRAVITATIONAL_CONSTANT * m_0 * m_1 / square(r)

def calculate_gravitational_force_vector(m_0:Quantity,
                                         m_1:Quantity,
                                         r:Quantity|ndarray) -> Quantity:
    """
    Calculates the gravitational force vector between two bodies given their
        mass and separation.

    Parameters
    ----------
    m_0 : Quantity
        First mass.
    m_1 : Quantity
        Second mass.
    r : Quantity|ndarray
        Seperation of center of masses, vector from m_0 to m_1.

    Returns
    -------
    Quantity
        The attractive gravitational force acting on the bodies.

    Notes
    -----
    Does not account for relativistic effects.
    """
    return -GRAVITATIONAL_CONSTANT * m_0 * m_1 * r / power(norm(r), 3)

def calculate_gravitational_acceleration_vector(m_0:Quantity,
                                                m_1:Quantity,
                                                r:ndarray|Quantity) -> Quantity:
    """
    Calculates the gravitational acceleration vector from one body toward
        another.

    m_0 : Quantity
        The first mass.
    m_1 : Quantity
        The second mass.
    r : ndarray|Quantity
        The separation vector from m_0 to m_1.
    """
    return -GRAVITATIONAL_CONSTANT * (m_0 + m_1) * r / power(norm(r), 3)

def calculate_gravitation_acceleration_earth(m_0:Quantity,
                                             m_1:Quantity,
                                             r:ndarray|Quantity) -> Quantity:
    """
    Approximates the gravitational acceleration of a satellite in Earth orbit.

    r : ndarray|Quantity
        The separation vector from m_0 to m_1.
    """
    return -EARTH_ACCEL_CONSTANT * r / power(norm(r), 3)

###############################################################################
###                                 CLASSES                                 ###
###############################################################################

@dataclass
class Orbit:
    """
    Class for simple eliptical orbits.
    """
    # Semi-major axis.
    alpha : Quantity = None
    # Eccentricity. [0, 1)
    eccen : Quantity = None
    # Inclination. Rising angle off equator.
    incln : Quantity = None
    # Right ascension.
    omega : Quantity = None
    # Argument of perigee. Angle offset at which perigee occurs, opening from 
    #   equatorial crossing.
    perig : Quantity = None
    # Time of perigee.
    tperi : Quantity = None

###############################################################################
###                                  MAIN                                   ###
###############################################################################

def main():
    pass

if __name__ == "__main__":
    main()

###############################################################################
###                                  NOTES                                  ###
###############################################################################
