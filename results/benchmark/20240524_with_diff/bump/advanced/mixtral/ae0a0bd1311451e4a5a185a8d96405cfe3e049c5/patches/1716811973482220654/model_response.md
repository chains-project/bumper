Here's a suggested patch for the client code:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains.containsString(java.lang.String.format("latest: digest: %s", original.digest())));
}
```

In this patch, I replaced the `new org.hamcrest.core.StringContains(false, java.lang.String.format("latest: digest: %s", original.digest()))` constructor with `new org.hamcrest.core.StringContains.containsString(java.lang.String.format("latest: digest: %s", original.digest()))` to fix the error message.

The `StringContains` constructor has been changed in the new library version to require a single argument of type `String`, instead of two arguments of type `boolean` and `String`. The `containsString` method is a new addition in the new library version that can be used to achieve the same functionality.