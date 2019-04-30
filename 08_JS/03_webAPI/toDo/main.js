const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector('#reverse_btn');
    const fetchButton = document.querySelector('#fetch_btn');
    const inputArea = document.querySelector('#add_todo_input');
    const button = document.querySelector('#add_todo_btn');





    // TODO: input, Add 버튼에 createTodo 와 이벤트 리스너를 잘 버무린다.
    const createTodo = (inputText, completed=false) => {
        const todoCard = document.createElement('div');

        todoCard.classList.add('ui', 'segment', 'todo-item');
        if (completed) todoCard.classList.add('secondary');


        // Card > Wrapper
        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');
        // Card > Wrapper > input (checkbox)
        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        input.checked = completed;

        input.addEventListener('click', e => {
            if (input.checked) {
                label.classList.add('completed-label');
                todoCard.classList.add('secondary');
            } else {
                label.classList.remove('completed-label');
                todoCard.classList.remove('secondary');
            }
        });

        const label = document.createElement('label');
        label.innerHTML = inputText;
        if (completed) label.classList.add('completed-label');

        const deleteIcon = document.createElement('i'); // <i></i>
        deleteIcon.classList.add('close', 'icon', 'delete-icon'); // <i class="close icon"></i>

        deleteIcon.addEventListener('click', e => {
            todoBox.removeChild(todoCard);
        });


        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);


        return todoCard
    };
// TODO: 버튼 만들고, 데이터 받아오게 이벤트 리스너 클릭 얍

    button.addEventListener('click', e => {
        todoBox.appendChild(createTodo(inputArea.value))
    });

    inputArea.addEventListener('keydown', e => {
        if (e.code === 'Enter') {
            todoBox.appendChild(createTodo(inputArea.value))
        }
    });


    reverseButton.addEventListener('click', e => {
        reverseTodos()
    });

    fetchButton.addEventListener('click', e => {
        const fetchData = (URL) => {
            fetch(URL)
                .then(res => res.json())
                .then(todos => {
                    for (const todo of todos) {
                        todoBox.appendChild(createTodo(todo.title, todo.completed));
                    }
                } )
        };
        fetchData('https://koreanjson.com/todos');
    });

    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll('.todo-item'));

        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild)
        }
        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo);
        }
    };



};

init();