-module(problem5).
-export([filter/1]).
-export([iterate/2]).

filter([H|T]) ->
    io:format("Filter Being Used Is: ~p\n", [H]),
    iterate(T, H).

iterate([H|T], Filter) ->
    RegExp = io:format("*~p*", [H]),
    case re:run(H, RegExp) of
        {match, Captured} -> io:format("Value Passes: ~p\n", [H]);
        nomatch -> io:format("Value Fails: ~p\n", [H])
    end,
    iterate(T, Filter).