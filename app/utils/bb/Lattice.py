import sys
import bpy
import os
def delete_all():
	for item in bpy.context.scene.objects:
		bpy.context.scene.objects.unlink(item)
	for item in bpy.data.objects:
		bpy.data.objects.remove(item)
	for item in bpy.data.meshes:
		bpy.data.meshes.remove(item)
	for item in bpy.data.materials:
		bpy.data.materials.remove(item)
def createLattice(scene,argvs):
	lattice = bpy.data.lattices.new("Lattice")
	lattice_ob = bpy.data.objects.new("LatticeObj",lattice)
	lattice_ob.location = (0.55,-0.63,0.5)
	#lattice_ob.show_x_ray = True
	for ob in scene.objects:
		if ob.type == 'MESH':
			mod = ob.modifiers.new("Lattice",'LATTICE')
			mod.object = lattice_ob
	scene.objects.link(lattice_ob)
	scene.objects.active = lattice_ob
	scene.update()

	lattice.interpolation_type_u = 'KEY_LINEAR'
	lattice.interpolation_type_v = 'KEY_CARDINAL'
	lattice.interpolation_type_w = 'KEY_BSPLINE'
	lattice.use_outside =False
	lattice.points_u =2
	lattice.points_v =2
	lattice.points_w =2
	s = 0.5
	s2 = float(argvs[6])
	s_z = float(argvs[7])
	s_y = float(argvs[8])
	s_x = float(argvs[9])
	points = [
		(-s,-s,-s),(s2+s_x,-s2+s_y,-s2+s_z),(-s,s,-s),(s2+s_x,s2+s_y,-s2+s_z),
		(-s,-s,s),(s2+s_x,-s2+s_y,s2+s_z),(-s,s,s),(s2+s_x,s2+s_y,s2+s_z)
	]
	bpy.context.scene.update()
	bpy.ops.object.mode_set(mode='EDIT')
	for n,pt in enumerate(lattice.points):
		for k in range(3):
			pt.co_deform[k] = points[n][k]
			#pass
	"""2cool"""
	lattice_2 = bpy.data.lattices.new("Lattice2")
	lattice_ob_2 = bpy.data.objects.new("LatticeObj2",lattice_2)
	lattice_ob_2.location = (0.55,0.5,0.5)
	#lattice_ob.show_x_ray = True
	for ob in scene.objects:
		if ob.type == 'MESH':
			mod = ob.modifiers.new("Lattice2",'LATTICE')
			mod.object = lattice_ob_2
	scene.objects.link(lattice_ob_2)
	scene.objects.active = lattice_ob_2
	scene.update()
	lattice_2.interpolation_type_u = 'KEY_LINEAR'
	lattice_2.interpolation_type_v = 'KEY_CARDINAL'
	lattice_2.interpolation_type_w = 'KEY_BSPLINE'
	lattice_2.use_outside =False
	lattice_2.points_u =2
	lattice_2.points_v =2
	lattice_2.points_w =2
	points = [
		(-s,-s,-s),(s2+s_x,-s2-s_y,-s2+s_z),(-s,s,-s),(s2+s_x,s2-s_y,-s2+s_z),
		(-s,-s,s),(s2+s_x,-s2-s_y,s2+s_z),(-s,s,s),(s2+s_x,s2-s_y,s2+s_z)
	]
	bpy.context.scene.update()

	for n,pt in enumerate(lattice_2.points):
		for k in range(3):
			pt.co_deform[k] = points[n][k]
			#pass

	return lattice_ob



if __name__ == "__main__":
	argvs = sys.argv
	LOAD_FILE = os.path.join(os.getcwd(),'app/static/OBJfile/boobs_flat.obj')
	delete_all()
	bpy.ops.import_scene.obj(filepath= LOAD_FILE)
	scene = bpy.context.scene
	lat = createLattice(scene,argvs)
	
	bpy.context.scene.objects.active = bpy.data.objects["Default"]
	bpy.ops.object.mode_set(mode='EDIT')
	#bpy.context.scene.update()
	'''	
	bpy.ops.mesh.mark_sharp()
	for i in range(10):
		bpy.ops.mesh.vertices_smooth()
	bpy.ops.object.mode_set(mode='OBJECT')
	'''
	EXP_FILE = "app/static/OBJfile/ex_boobs.obj"
	#printOBJ()
	savePath = os.path.abspath(os.path.dirname(__file__))
	bpy.path.relpath(savePath)
	bpy.ops.export_scene.obj(filepath=EXP_FILE)
	#bpy.ops.export_scene.obj(filepath="OKOK.obj")
	#bpy.ops.wm.save_as_mainfile(filepath="OKOK.blend",relative_remap=True)
	#add_cone()
	#add_cube_by_data()
	#bpy.data.objects["Default"].data.vertices[0].co.x +=20.0
	#bpy.ops.object.editmode_toggles()
	#bpy.ops.object.mode_set(mode='EDIT')
	#bpy.ops.translate(value=(0,0,2),constraint_axis=(False,False,False),constraint_orientation='GLOBAL',mirror = False,proportional='DISABLED',proportional_edit_falloff='SMOOTH',proportional_size=1)

