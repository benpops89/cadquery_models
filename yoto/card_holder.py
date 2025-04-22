import cadquery as cq

width = 100
depth = 130
height = 45
wall_thickness = 5
corner_radius = 6

# Create the outer shell
outer = cq.Workplane("XY").rect(width, depth).extrude(height)

# Create the inner shell
inner = (
    cq.Workplane("XY")
    .rect(width - 2 * wall_thickness, depth - 2 * wall_thickness)
    .extrude(height - wall_thickness)
    .translate((0, 0, wall_thickness))
)

# Remove the inner shell from outer
holder = outer.cut(inner)

holder.export("holder.stl")
