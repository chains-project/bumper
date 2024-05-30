Here is the proposed patch for the client code:
```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```
The only change made is in the `assertThat` statement, where the `StringContains` constructor is now called with a single `String` argument instead of a `boolean` and a `String`. This is because the `StringContains` constructor that accepts a `boolean` argument has been removed in the new library version.