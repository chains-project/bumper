Based on the error message and the changes in the library version, it seems that the `getClassInfo` method in `CoverageDatabase` now expects a single `ClassName` instead of a collection. Here's a possible patch for the `createSummaryData` method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In this patch, we extract the `mutatedClass` from the `ClassMutationResults` and pass it to the `getClassInfo` method of `CoverageDatabase`. We then use the returned `ClassInfo` object to create the `MutationTestSummaryData`. Note that we use the new `ClassInfo` class from the `org.pitest.classinfo` package instead of the old `ClassInfo` class from the `org.pitest.coverage` package.