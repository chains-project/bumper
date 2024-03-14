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
                final String reqLine,
                final Iterable<Map.Entry<String, String>> headers,
                final Publisher<ByteBuffer> body
            ) {
                return StandardRs.OK;
            }
        },
        (headers, rline) -> CompletableFuture.completedFuture(
            new AuthScheme.Result() {
                @Override
                public Optional<Authentication.User> user() {
                    return Optional.of(new Authentication.User("alice"));
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
```
In the code above, I replaced the parameter name `line` with `reqLine` in the `response` method. The error message indicated that there was a symbol it could not find, which was likely due to the `line` parameter in the `response` method shadowing the `line` variable in the test method. By renaming the parameter to `reqLine`, the shadowing is resolved and the correct `line` variable is used.