Here's a possible patch for the client code that should fix the error:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    final boolean contains = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("latest: digest: " + original.digest()));
    org.junit.jupiter.api.Assertions.assertFalse(contains);
}
```
The changes I made are:

* Replace the `assertThat` method call with two separate assertions: one that checks that the output contains the expected string, and another that checks that the `contains` variable is `false`. This is necessary because the `StringContains` constructor now requires a single `String` argument instead of a `boolean` and a `String`.
* Add a line to set the `contains` variable to the result of calling the `contains` method on the `output` string. This is needed to satisfy the new `StringContains` constructor.
* Add an import statement for `org.junit.jupiter.api.Assertions` at the top of the file, if it's not already there, to make the `assertFalse` method call work.

Note that these changes preserve the behavior of the original code, but use a different approach to perform the assertions. This is necessary because of the changes in the library.