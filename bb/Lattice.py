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
	s2 = float(argvs[4])
	s_z = float(argvs[5])
	s_y = float(argvs[6])
	s_x = float(argvs[7])
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
	bpy.ops.object.mode_set(mode='EDIT')
	for n,pt in enumerate(lattice_2.points):
		for k in range(3):
			pt.co_deform[k] = points[n][k]
			#pass
	
	return lattice_ob

def printOBJ():
	LOAD10 = "/home/blender/test.obj"
	name = os.path.basename(LOAD10)
	realpath = os.path.realpath(os.path.expanduser(LOAD10))
	fp = open(realpath,'w')
	me = bpy.data.objects["Default"].data
	for v in me.vertices:
		fp.write("v %.5f %.5f %.5f\n" % (v.co.x,v.co.y,v.co.z))
	temp_me = me.uv_layers.active.data
	#for f in temp_me:
	#	fp.write("vt %.5f %.5f\n" % (f.uv[0],f.uv[1]))
	if len(me.uv_layers.active.data)>0:
		#uvtex=me.uv_textures[0]
		count = 0
		for f in me.polygons:
			#data = temp_me[f.index]
			data = temp_me[count]
			fp.write("vt %.5f %.5f\n" % (data.uv[0],data.uv[1]))
			count = count +1
			data = temp_me[count]
			fp.write("vt %.5f %.5f\n" % (data.uv[0],data.uv[1]))
			count = count +1
			data = temp_me[count]
			fp.write("vt %.5f %.5f\n" % (data.uv[0],data.uv[1]))
			count = count +1
			if len(f.vertices) == 4:
				data=temp_me[count]
				fp.write("vt %.5f %.5f\n" % (data.uv[0],data.uv[1]))
				count = count + 1

		#fp.write("ok %s\n"%(len(temp_me)))
		#fp.write("count %s"%(count))
		vt =1
		for f in me.polygons:
			vs = f.vertices
			fp.write("f %d/%d %d/%d %d/%d" % (vs[0]+1,vt,vs[1]+1,vt+1,vs[2]+1,vt+2))
			vt += 3
			if len(f.vertices) == 4:
				fp.write(" %d/%d\n" % (vs[3]+1,vt))
				vt += 1
			else:
				fp.write("\n")
	fp.close()
	return 0
		
		

if __name__ == "__main__":
	argvs = sys.argv
	LOAD_FILE = "/var/www/html/mrdoob-three.js/bb/boobs_dis.obj"
	delete_all()
	bpy.ops.import_scene.obj(filepath= LOAD_FILE)
	scene = bpy.context.scene
	lat = createLattice(scene,argvs)
	EXP_FILE = "ex_boobs.obj"
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
	
