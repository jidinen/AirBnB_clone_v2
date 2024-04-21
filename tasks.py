from invoke import task
@task
def code(ctx, foldername, archive_name):
    ctx.run("echo {archive_name}")

# Calling the task using invoke command
if __name__ == "__main__":
    code()
