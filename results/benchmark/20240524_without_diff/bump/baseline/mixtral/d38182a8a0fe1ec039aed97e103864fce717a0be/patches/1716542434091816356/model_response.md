Here's the patched version of the `testScope` method that should fix the error:

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
```

The change is to pass an empty string as the second argument to the `AuthUser` constructor. According to the library changes, the constructor now requires two arguments, and the second one is optional and defaults to an empty string. Since the original code did not pass any second argument, it needs to be updated to pass an empty string.