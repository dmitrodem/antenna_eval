all:
	openscad -D object=1 -o 01_splitter.dxf splitter.scad
	openscad -D object=2 -o 02_feedline.dxf splitter.scad
	openscad -D object=3 -o 03_splitter_and_feedline.dxf splitter.scad
	openscad -D object=4 -o 04_slots.dxf splitter.scad
	openscad -D object=5 -o 05_small_patch.dxf splitter.scad
	openscad -D object=6 -o 06_large_patch.dxf splitter.scad
	./export_step.py 01_splitter.dxf 01_splitter.step
	./export_step.py 02_feedline.dxf 02_feedline.step
	./export_step.py 03_splitter_and_feedline.dxf 03_splitter_and_feedline.step
	./export_step.py 04_slots.dxf 04_slots.step
	./export_step.py 05_small_patch.dxf 05_small_patch.step
	./export_step.py 06_large_patch.dxf 06_large_patch.step
clean:
	-rm -rf *.dxf *.step

.PHONY: all clean
