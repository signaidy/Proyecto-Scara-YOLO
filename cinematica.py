"""Basic SCARA geometry helpers for future D-H work."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import cos, radians, sin


@dataclass
class DHParameter:
    joint: str
    a_prev_cm: float
    alpha_prev_deg: float
    d_cm: float
    theta_deg: float
    joint_type: str

    def to_dict(self) -> dict[str, float | str]:
        return asdict(self)


def build_scara_dh_template(link_1_cm: float, link_2_cm: float, z_offset_cm: float = 0.0) -> list[DHParameter]:
    """Create a minimal D-H table scaffold for a didactic 3-DOF SCARA."""

    return [
        DHParameter("q1", 0.0, 0.0, z_offset_cm, 0.0, "revolute"),
        DHParameter("q2", link_1_cm, 0.0, 0.0, 0.0, "revolute"),
        DHParameter("q3", link_2_cm, 0.0, 0.0, 0.0, "prismatic_or_equivalent"),
    ]


def planar_forward_kinematics(
    q1_deg: float,
    q2_deg: float,
    link_1_cm: float,
    link_2_cm: float,
) -> tuple[float, float]:
    """Compute the planar XY position for a 2R SCARA arm."""

    q1 = radians(q1_deg)
    q2 = radians(q2_deg)
    x = link_1_cm * cos(q1) + link_2_cm * cos(q1 + q2)
    y = link_1_cm * sin(q1) + link_2_cm * sin(q1 + q2)
    return (x, y)

