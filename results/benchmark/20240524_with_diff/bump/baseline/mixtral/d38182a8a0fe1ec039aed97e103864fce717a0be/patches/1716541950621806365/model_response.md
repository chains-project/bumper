Here's the fixed version of the `testScope` method:

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

class AuthUser implements com.artipie.http.auth.AuthUser {
    private final String name;

    AuthUser(String name) {
        this.name = name;
    }

    @Override
    public String authContext() {
        return null;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof AuthUser)) return false;
        AuthUser authUser = (AuthUser) o;
        return Objects.equals(name, authUser.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }

    @Override
    public String name() {
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}
```

The main change is the creation of the `AuthUser` class, which implements the new `com.artipie.http.auth.AuthUser` interface. This class wraps a username and provides the necessary implementations for the interface methods. The `testScope` method then uses this `AuthUser` class instead of the removed `Authentication.User` class.