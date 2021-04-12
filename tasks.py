from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/watchdough.py")

@task
def start_real(ctx):
    ctx.run("python3 src/watchdough.py R1")

@task
def test(ctx):
    ctx.run('pytest src')

@task
def coverage_report(ctx):
    ctx.run('coverage run --branch -m pytest src')
    ctx.run('coverage report -m')