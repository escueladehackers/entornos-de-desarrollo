from invoke import Collection, task

@task(default=True)
def saluda(ctx):
  print("¡Mi primera tarea con invoke!") 


namespace = Collection(saluda)
