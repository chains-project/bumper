Here's the fixed method with the error resolved:

```java
@org.junit.jupiter.api.Test
void shouldPullPushedByTag() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remote());
    boolean notContains = !output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remote()), notContains);
}
```

The issue was caused by using the `StringContains` constructor with a boolean flag, which is not valid. Instead, I have created a separate variable `notContains` to store the boolean value and used the `contains` method of the String class to check if the output doesn't contain the specific string.