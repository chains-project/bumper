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
        ).handleResponse((status, headers, body) -> {
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
            return CompletableFuture.completedFuture(true);
        }).join();
    }
```
The main change is that the `response` method of `AuthScopeSlice` is now handled using the `handleResponse` method, which allows us to define a callback that will be called when the response is received. This callback is where we can add the assertions that were previously in the `toCompletableFuture().join()` call.

Note that the `handleResponse` method is an added library method identified with `++`, so it should be available in the new version of the library.