sum_list([], 0).                   % Сумма пустого списка равна 0
sum_list([Head | Tail], Sum) :-    % Сумма списка с головой Head и хвостом Tail
    sum_list(Tail, TailSum),       % Вычисляем сумму хвоста списка
    Sum is Head + TailSum.         % Сумма списка равна сумме головы и сумме хвоста

?- sum_list([1,2,3,4,5,6,7,8,9,10], X),

    write('Суммы элементов списка: '),
    writeln(X),
