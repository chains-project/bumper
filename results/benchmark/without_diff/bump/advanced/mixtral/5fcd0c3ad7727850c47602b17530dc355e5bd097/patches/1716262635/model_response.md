Here is a possible patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which is a new method added in the `CoverageDatabase` interface. This method takes a single `ClassName` argument and returns the corresponding `ClassInfo` object. I also changed the argument of `getClassInfoFor` method to `data.getMutatedClass()` which is of type `ClassName`. This should resolve the "cannot find symbol" error.