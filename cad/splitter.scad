include <BOSL2/std.scad>
za_width = 1.9;
za_length = 10;
za_fold_depth = 7;
za_fold_radius = 1.0;

zb_width = 1.18;
zb_length = 21.86;

microstrip_width = 1.18;
port_extension = 5.0;
port_separation = 50.0;

gnd_width = 100.0;

feed_offset = 10;

slot_length1 = 8.7;
slot_width1  = 1.0;

slot_length2 = 5.0;
slot_width2  = 4.5;

slot_offset = 14.5;

patch1_width = 36.0;

patch2_width = 48.5;

stub_length1 = 3.0;
stub_length2 = 1.0;
stub_length3 = 10.0;

object = 2;

point1 = [-feed_offset, zb_length/2];
point2 = [-feed_offset-za_length, zb_length/2];
point3 = zrot(45, p = [slot_offset, 0]);


module splitter() {
  p1 = turtle([
               "turn", 180,
               "move", za_length/3-za_fold_radius,
               "arcleft", za_fold_radius,
               "move", za_fold_depth - 2*za_fold_radius,
               "arcright", za_fold_radius,
               "untilx", 0],
              state = [[[za_length/2, zb_length/2]],[1,0],90,0]);
  p2 = xmove(za_length/2, p = turtle(["turn", 90, "move", zb_length/2]));

  xmove(-feed_offset)
    xmove(-za_length/2)
    yflip_copy()
    xflip_copy()
    union() {
    stroke(p1, width = za_width);
    stroke(p2, width = zb_width);
  }
}

module feedlines_splitter(standalone = true) {
  p3 = turtle([
               "move", port_extension,
               "turn", 45,
               "untily", port_separation/2,
               "turn", -45,
               "untilx", gnd_width/2],
              state = [[point1],[1,0],90,0]);
  p4 = turtle([
               "turn", 180,
               "move", port_extension,
               "turn", -45,
               "untily", port_separation/2,
               "turn", 45,
               "untilx", -gnd_width/2],
              state = [[point2],[1,0],90,0]);

  yflip_copy()
    union() {
    if (standalone) {
    stroke(p3, width = zb_width, endcap2 = "butt");
    }
    stroke(p4, width = zb_width, endcap2 = "butt");
  }
}

module slots() {
  color("blue")
    down(1)
    yflip_copy()
    zrot(45)
    xmove(slot_offset)
    rect(size = [slot_width1, slot_length1]) {
    yflip_copy()
      position(BACK) {
      rect(size = [slot_width2, slot_length2], anchor = FRONT);
    }
  }
}

module patch1() {
  color("green") rect(size = [patch1_width, patch1_width]);
}

module patch2() {
  color("cyan") rect(size = [patch2_width, patch2_width]);
}

module feedlines_antenna(standalone = true) {
  p5 = turtle([
               "turn", 45,
               "move", stub_length1,
               "turn", 45,
               "move", stub_length2,
               "turn", 45,
               "move", stub_length3],
              state = [[point3],[1,0],90,0]);
  p6 = turtle([
               "turn", 45+180,
               "move", feed_offset/2,
               "turn", -45,
               "untilx", 0,
               "turn", -45,
               "untily", zb_length/2,
               "turn", 45,
               "untilx", point1[0]],
              state = [[point3],[1,0],90,0]);
  p7 = turtle([
               "turn", 45+90,
               "untily", port_separation/2,
               "turn", 45,
               "untilx", -gnd_width/2],
              state = [[point1],[1,0],90,0]);

  yflip_copy() {
    stroke(p5, width = microstrip_width);
    stroke(p6, width = microstrip_width);
    if (standalone) {
      stroke(p7, width = microstrip_width, endcap2 = "butt");
    }
  }
}

if (object == 1) {
  // standalone splitter
  splitter();
  feedlines_splitter(true);
 } else if (object == 2) {
  // standalone antenna feed
  feedlines_antenna(true);
 } else if (object == 3) {
  // splitter + antenna feed
  splitter();
  feedlines_splitter(false);
  feedlines_antenna(false);
 } else if (object == 4) {
  // slots
  slots();
 } else if (object == 5) {
  // smaller patch
  patch1();
 } else if (object == 6) {
  // larger patch
  patch2();
 }
