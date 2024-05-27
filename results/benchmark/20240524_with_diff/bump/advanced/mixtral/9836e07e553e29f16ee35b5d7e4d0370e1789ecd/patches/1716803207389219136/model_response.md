Here's the updated code that should resolve the error:

```java
@org.junit.jupiter.api.Test
void shouldPullPushedByTag() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remote());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remote()));
}
```

The error message indicates that the constructor `StringContains` expects a single argument of type `String`, but it's being passed two arguments of type `boolean` and `String`. To fix this, I've replaced the usage of `StringContains` with a call to `contains` method on the `output` string, and then used `StringContains` with a single argument that includes the expected substring.