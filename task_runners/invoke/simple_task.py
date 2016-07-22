from invoke import Collection, task

@task
def saluda(ctx):
  print("¡Mi primera tarea con invoke!") 


namespace = Collection(saluda)
