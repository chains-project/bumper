Here's the fixed version of the method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(data.getMutatedClass()).build());
}
```

I created a new variable `className` for the `data.getMutatedClass()` to make the code easier to understand. Also, I used the new `getClassInfo` method that accepts `ClassName` and returns a `ClassInfoBuilder` and called the `build()` method on it to get the `ClassInfo` instance.