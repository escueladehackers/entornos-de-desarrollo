from invoke import task

@task(default=True)
def clean(ctx, docs=False, bytecode=False, extra=''):
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        ctx.run("rm -rf %s" % pattern)

@task(clean)
def build(ctx, docs=False):
    ctx.run("python setup.py build")
    if docs:
        ctx.run("sphinx-build docs docs/_build")
