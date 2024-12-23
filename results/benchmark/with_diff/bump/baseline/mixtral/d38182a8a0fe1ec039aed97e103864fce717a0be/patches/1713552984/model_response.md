Here is the proposed patch:
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
                                return Optional.of(new AuthUser("alice"));
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
The only change I made is to replace `Authentication.User` with `AuthUser` in the lambda passed to `AuthScopeSlice` constructor. This is because the `Authentication.User` class has been removed in the new library version and replaced with `AuthUser`. The `AuthUser` class has a similar interface to `Authentication.User`, so the change should not affect the functionality of the code.