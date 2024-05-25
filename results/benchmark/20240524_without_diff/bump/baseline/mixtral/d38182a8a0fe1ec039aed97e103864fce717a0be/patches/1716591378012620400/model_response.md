Here's the patched `testScope` method. I added a null check to avoid the "cannot find symbol" error. It seems like the error is caused by the `Headers.EMPTY` constant being null or not imported properly.

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
    ).response(line, (Headers.EMPTY != null) ? Headers.EMPTY : ImmutableHeaders.of(), Content.EMPTY).send(
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

If the issue persists, please check the import statement for `Headers.EMPTY` and make sure it is correctly imported.