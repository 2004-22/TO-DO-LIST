# Task Tracker 
Sample solution for the [ask-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh.](https://roadmap.sh/)

# How to run

Clone the repository and run the following command in the terminal:
https://github.com/2004-22/TO-DO-LIST.git
cd 2004-22/TO-DO-LIST
mv app.py todo-list
chmod +x todo-list

Run the following command to build and run the project:

./todo-list --help # To see the list of available commands

`# To add a task`
./todo-list add "Buy groceries"

 `# To update a task`
./todo-list update 1 "Buy groceries and cook dinner"

`# To delete a task`
./todo-list delete 1

`# To mark a task as in progress/done/todo`
./todo-list mark-in-progress 1
./todo-list mark-done 1
./todo-list mark-todo 1

`# To list all tasks`
./todo-list list
./todo-list list-done
./todo-list list-pending
./todo-list list-in-progress
