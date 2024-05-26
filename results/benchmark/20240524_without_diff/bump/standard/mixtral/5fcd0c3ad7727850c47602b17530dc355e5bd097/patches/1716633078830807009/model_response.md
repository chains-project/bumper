Here is a fixed version of the method that should resolve the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this version, I replaced the `getClassInfo` method with `getClassInfoFor`, which is a new method added in the `CoverageDatabase` class. This method takes a single `ClassName` argument and returns the corresponding `ClassInfo` object. This should resolve the error message you were seeing.