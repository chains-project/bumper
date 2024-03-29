Sure, here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    if (classInfo == null) {
      return new MutationTestSummaryData(data.getFileName(),
          data.getMutations(), Collections.emptyList());
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo.getElements());
  }
```
In this patch, we first check if `classInfo` is `null` before trying to access its `getElements()` method. If `classInfo` is `null`, we return a new `MutationTestSummaryData` object with an empty list of elements. This should prevent the `cannot find symbol` error from occurring.

Note that this patch assumes that if `classInfo` is `null`, then the class in question has no elements, and so an empty list is a reasonable substitute. If this assumption is incorrect, then the patch may need to be modified accordingly.