Here is the proposed patch:
```java
@Test
void largeImageUploadWorks() throws Exception {
    boolean pushed = false;
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        pushed = output.contains("Pushed");
        MatcherAssert.assertThat(pushed, Matchers.is(true));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```
In this patch, we create a new variable `pushed` to store the result of `output.contains("Pushed")`, and then use `MatcherAssert.assertThat` to check if `pushed` is `true`. This way, we avoid the error caused by the updated library, which no longer accepts a boolean value in the `StringContains` constructor.