```java
@Override
        public Slice slice(final String action) {
            final String token = TestAuthentication.ALICE.token();
            final AstoDocker astoDocker = new AstoDocker(new InMemoryStorage());
            final Permissions.Single permissions = new Permissions.Single(TestAuthentication.ALICE.name(), action);
            final BearerAuthScheme bearerAuthScheme = new BearerAuthScheme(
                token1 -> CompletableFuture.completedFuture(
                    Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                        .filter(user -> token1.equals(token))
                        .map(user -> new Authentication.User(user.name()))
                        .findFirst()
                ),
                ""
            );
            return new DockerSlice(astoDocker, permissions, bearerAuthScheme);
        }
```