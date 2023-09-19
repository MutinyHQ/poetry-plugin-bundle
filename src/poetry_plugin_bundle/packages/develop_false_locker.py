from poetry.packages.locker import Locker
from poetry.repositories.lockfile_repository import LockfileRepository


class DevelopFalseLocker(Locker):
    def __init__(self, base_locker: Locker):
        super().__init__(base_locker._lock, base_locker._local_config)

    def locked_repository(self) -> LockfileRepository:
        repository = super().locked_repository()
        no_develop_repository = LockfileRepository()
        for package in repository.packages:
            no_develop_package = package.clone()
            no_develop_package.develop = False
            no_develop_repository.add_package(no_develop_package)
        return no_develop_repository
