import os 
from pathlib import Path
from icecream import ic

def git_create_worktree(git_folder: str, branch_name: str):
    ic(os.getcwd(), git_folder, Path(git_folder).absolute(), branch_name)
    branch_folder = Path(git_folder).parent / 'tmp' / branch_name
    if branch_folder.exists():
        return 
    else:
        try:
            cwd = os.getcwd()
            os.chdir(git_folder)
            os.system(f'git worktree add ../tmp/{branch_name}')
        except:
            pass 
        finally:
            os.chdir(cwd)

def test():
    git_create_worktree('/home/niraj/Documents/python/gitdir/test/icecream/icecream',
                        'branch1')

if __name__ == '__main__':
    test()