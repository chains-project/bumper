Here is a fixed version of the method that should resolve the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

The change I made is to replace the `getClassInfo` method with `getClassInfoFor` method, which is a new method added in the `CoverageDatabase` class. This should resolve the "cannot find symbol" error.