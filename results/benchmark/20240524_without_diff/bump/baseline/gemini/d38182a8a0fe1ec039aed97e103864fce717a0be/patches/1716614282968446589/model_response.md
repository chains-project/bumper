```java
  @Override
                    public Optional<Authentication.User> user() {
                        // Get the user name from the authentication header.
                        String userName = authentication.getHeader("X-User");

                        // If the user name is not present, return an empty optional.
                        if (userName == null) {
                            return Optional.empty();
                        }

                        // Create a new user object with the given user name.
                        Authentication.User user = new Authentication.User(userName);

                        // Return the user object wrapped in an optional.
                        return Optional.of(user);
                    }
```