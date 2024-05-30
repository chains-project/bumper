Here is the proposed patch for the failing client code:
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
The only change made is in the `assertThat` statement, where we removed the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor with a `boolean` argument has been removed in the new library version, and it now only accepts a single `String` argument.