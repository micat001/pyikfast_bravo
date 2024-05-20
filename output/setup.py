from distutils.core import Extension, setup

import setuptools

extra_objects = [
    "/usr/lib/x86_64-linux-gnu/lapack/liblapack.a",
    "/usr/lib/x86_64-linux-gnu/libgfortran.so.5.0.0",
    "/usr/lib/x86_64-linux-gnu/blas/libblas.a",
]


def main():
    setup(
        name="pyikfast_bravo7",
        version="0.0.1",
        description="ikfast wrapper",
        author="Cyberbotics",
        author_email="support@cyberbotics.com",
        ext_modules=[
            Extension(
                "pyikfast_bravo7",
                ["ikfast_robot.cpp", "pyikfast.cpp"],
                extra_objects=extra_objects,
            )
        ],
        setup_requires=["wheel"],
    )


if __name__ == "__main__":
    main()
