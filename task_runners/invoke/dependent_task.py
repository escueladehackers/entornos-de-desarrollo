from invoke import Collection, task

@task
def despedirse(ctx):
  print("Fue bueno mientras duro")

@task(despedirse)
def die(ctx):
  print("Adios mundo cruel")

@task(post=[die], default=True)
def saluda(ctx):
  print("¡Mi primera tarea con invoke!") 

