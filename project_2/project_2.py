import os
root1="testdir"
extension1=".c"
root2="testdir/subdir3"
extension2=".h"
extension3='.d'
def list_path(cur,out,extension):
    if not os.path.isfile(cur) and not os.path.isdir(cur) :
        return "Negative"
    if cur.endswith(extension):
        out.append(cur)
    elif os.path.isdir(cur):
        for active in  os.listdir(cur):
            active=os.path.join(cur,active)
            list_path(active,out,extension)
    return out
def pri_val(out):
    if out=="Negative":
        print("Enter proper exiisting Directory")
        return
    if len(out)==0:
        print("No files found")
    else:
        print(*out,sep='\n')
    print("\n")
out=list_path(root1,[],extension1)
pri_val(out)
out=list_path(root2,[],extension2)
pri_val(out)
out=list_path(root1,[],extension3)
pri_val(out)
out=list_path("",[],extension3)
pri_val(out)
out=list_path("hi/wrong",[],extension3)
pri_val(out)