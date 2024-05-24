Here's the fixed version of the `largeImageUploadWorks` method using the new library version:

```java
@Test
void largeImageUploadWorks() throws Exception {
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        MatcherAssert.assertThat(output, new StringContains("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```

The change is in the `MatcherAssert.assertThat` line. Instead of using `new StringContains(false, "Pushed")`, I used `new StringContains("Pushed")`. This is because the constructor for `StringContains` no longer accepts a boolean parameter in the new library version.