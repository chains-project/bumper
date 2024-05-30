Here's the updated code that should fix the error:

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

The error message indicates that the `StringContains` constructor now takes only one argument, instead of two. To fix this, I replaced the `StringContains` constructor with a `contains` method from the `String` class to check if the output contains the expected string. Additionally, I updated the `assertThat` method call to use the new `StringContains` constructor.