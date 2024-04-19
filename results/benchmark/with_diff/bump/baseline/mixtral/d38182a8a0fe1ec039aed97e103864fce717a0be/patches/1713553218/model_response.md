Here's a possible patch for the failing client code:

```java
@Test
void testScope() {
    final String line = "GET /resource.txt HTTP/1.1";
    final String action = "foo:bar:baz";
    final AtomicReference<String> caction = new AtomicReference<>();
    final AtomicReference<String> cline = new AtomicReference<>();
    new AuthScopeSlice(
        new ScopeSlice() {
            @Override
            public Scope scope(final String rqline) {
                cline.set(rqline);
                return new Scope.FromString(action);
            }

            @Override
            public Response response(
                final String line,
                final Iterable<Map.Entry<String, String>> headers,
                final Publisher<ByteBuffer> body
            ) {
                return StandardRs.OK;
            }
        },
        (headers, rline) -> CompletableFuture.completedFuture(
            new AuthScheme.Result() {
                @Override
                public Optional<AuthUser> user() {
                    return Optional.of(new AuthUser("alice", ""));
                }

                @Override
                public String challenge() {
                    return "";
                }
            }
        ),
        (user, act) -> {
            caction.set(act);
            return true;
        }
    ).response(line, Headers.EMPTY, Content.EMPTY).send(
        (status, headers, body) -> CompletableFuture.allOf()
    ).toCompletableFuture().join();
    MatcherAssert.assertThat(
        "Request line passed to slice",
        cline.get(),
        new IsEqual<>(line)
    );
    MatcherAssert.assertThat(
        "Scope passed as action to permissions",
        caction.get(),
        new IsEqual<>(action)
    );
}

record AuthUser(String name, String authContext) { }
```

The main change is to replace `Authentication.User` with `AuthUser`, which is a new class added in the updated library version. I've defined `AuthUser` as a record with two fields, `name` and `authContext`, to match the constructor and methods of the original `Authentication.User` class.

Note that the `AuthUser` class does not have a `groups()` method, which was present in the original `Authentication.User` class. If you need this functionality, you may need to modify the code accordingly.

I've also updated the lambda expression that creates an `AuthScheme.Result` object to use the new `AuthUser` class.

Finally, I've added the `AuthUser` record definition at the end of the method. If you prefer, you can define `AuthUser` as a top-level class or inner class in your code.