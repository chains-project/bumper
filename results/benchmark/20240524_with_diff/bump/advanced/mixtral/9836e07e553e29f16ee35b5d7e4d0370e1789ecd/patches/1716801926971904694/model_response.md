Here's a possible patch for the client code that should fix the error:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(org.hamcrest.CoreMatchers.containsString(String.format("latest: digest: %s", original.digest()))));
}
```
The patch changes the way the `StringContains` matcher is created, by using the `containsString` method instead of the overloaded constructor. This resolves the error caused by the removal of the constructor that takes a boolean argument.