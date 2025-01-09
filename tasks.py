from invoke import task
import os

@task
def python(ctx):
    """ """
    ctx.run("which python" if os.name != "nt" else "where python")

@task
def git(ctx, message):
    ctx.run(f"git add .", echo=True)
    ctx.run(f"git commit -m '{message}'", echo=True)
    ctx.run(f"git push", echo=True)