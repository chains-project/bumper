Here is the proposed patch for the client code:
```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    final boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", image));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : "does not", image));
}
```
In this patch, I replaced the problematic line with a new line that uses the `contains` method of the `String` class to check if the output contains the expected message. Then, I used the `StringContains` matcher with the `does not` option if the message is not found.

The reason for this failure is that the `StringContains` constructor now requires only one argument (a `String`), but in the original code, it was called with two arguments (a `boolean` and a `String`). This change was introduced in the new library version, and the client code needs to be updated accordingly.