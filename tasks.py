from invoke import task


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    return black(c, False)


@task(aliases=["cf", "fc"])
def check_format(c):
    return black(c, True)


@task(aliases=["t"])
def test(c):
    return c.run("pytest")


@task(aliases=["lp"])
def lint_python(c):
    return c.run("pycodestyle .")


@task(aliases=["ly"])
def lint_yaml(c):
    return c.run("yamllint .")


@task(aliases=["l"], pre=[lint_python, lint_yaml])
def lint(c):
    pass
