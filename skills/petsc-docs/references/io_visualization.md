# Petsc-Docs-Full-Raw - Io Visualization

**Pages:** 435

---

## Graphics (Draw)#

**URL:** https://petsc.org/release/manualpages/Draw/

**Contents:**
- Graphics (Draw)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscDraw classes are used to produce simple graphics, with, for example X Windows.

PetscDrawGetMarkerType

PetscDrawSetMarkerType

PetscDrawStringCentered

PetscDrawStringVertical

PetscDrawBarSetFromOptions

PetscDrawBarSetLimits

PetscDrawGetBoundingBox

PetscDrawGetCurrentPoint

PetscDrawGetMouseButton

PetscDrawGetWindowSize

PetscDrawHGAddWeightedValue

PetscDrawHGIntegerBins

PetscDrawHGSetNumberBins

PetscDrawLGAddCommonPoint

PetscDrawLGGetDimension

PetscDrawLGSetDimension

PetscDrawLGSetFromOptions

PetscDrawLGSetUseMarkers

PetscDrawPopCurrentPoint

PetscDrawPushCurrentPoint

PetscDrawResizeWindow

PetscDrawSPAddPointColorized

PetscDrawSPGetDimension

PetscDrawSPSetDimension

PetscDrawSetCurrentPoint

PetscDrawSetDoubleBuffer

PetscDrawSetFromOptions

PetscDrawSetSaveFinalImage

PetscDrawSetSaveMovie

PetscDrawTensorContour

PetscDrawViewFromOptions

PetscViewerDrawGetDraw

PetscViewerDrawGetDrawLG

PetscDrawAxisGetLimits

PetscDrawAxisSetColors

PetscDrawAxisSetHoldLimits

PetscDrawAxisSetLabels

PetscDrawAxisSetLimits

PetscDrawCheckResizedWindow

PetscDrawCollectiveBegin

PetscDrawCollectiveEnd

PetscDrawGetCoordinates

PetscDrawGetSingleton

PetscDrawLGSetOptionsPrefix

PetscDrawLineGetWidth

PetscDrawLineSetWidth

PetscDrawPointSetSize

PetscDrawRestoreSingleton

PetscDrawSetCoordinates

PetscDrawSetOptionsPrefix

PetscDrawSplitViewPort

PetscDrawStringGetSize

PetscDrawStringSetSize

PetscDrawTensorContourPatch

PetscDrawViewPortsCreate

PetscDrawViewPortsCreateRect

PetscDrawViewPortsDestroy

PetscDrawViewPortsSet

PetscViewerDrawGetDrawAxis

PetscViewerDrawGetDrawType

PetscViewerDrawSetDrawType

PetscDrawCoordinateToPixel

PetscDrawFinalizePackage

PetscDrawIndicatorFunction

PetscDrawInitializePackage

PetscDrawPixelToCoordinate

PetscDrawUtilitySetCmap

PetscDrawUtilitySetGamma

PetscXIOErrorHandlerFn

PetscDrawAxisGetLimits

PetscDrawAxisSetColors

PetscDrawAxisSetHoldLimits

PetscDrawAxisSetLabels

PetscDrawAxisSetLimits

PetscDrawBarSetFromOptions

PetscDrawBarSetLimits

PetscDrawCheckResizedWindow

PetscDrawCollectiveBegin

PetscDrawCollectiveEnd

PetscDrawCoordinateToPixel

PetscDrawFinalizePackage

PetscDrawGetBoundingBox

PetscDrawGetCoordinates

PetscDrawGetCurrentPoint

PetscDrawGetMarkerType

PetscDrawGetMouseButton

PetscDrawGetSingleton

PetscDrawGetWindowSize

PetscDrawHGAddWeightedValue

PetscDrawHGIntegerBins

PetscDrawHGSetNumberBins

PetscDrawIndicatorFunction

PetscDrawInitializePackage

PetscDrawLGAddCommonPoint

PetscDrawLGGetDimension

PetscDrawLGSetDimension

PetscDrawLGSetFromOptions

PetscDrawLGSetOptionsPrefix

PetscDrawLGSetUseMarkers

PetscDrawLineGetWidth

PetscDrawLineSetWidth

PetscDrawPixelToCoordinate

PetscDrawPointSetSize

PetscDrawPopCurrentPoint

PetscDrawPushCurrentPoint

PetscDrawResizeWindow

PetscDrawRestoreSingleton

PetscDrawSPAddPointColorized

PetscDrawSPGetDimension

PetscDrawSPSetDimension

PetscDrawSetCoordinates

PetscDrawSetCurrentPoint

PetscDrawSetDoubleBuffer

PetscDrawSetFromOptions

PetscDrawSetMarkerType

PetscDrawSetOptionsPrefix

PetscDrawSetSaveFinalImage

PetscDrawSetSaveMovie

PetscDrawSplitViewPort

PetscDrawStringCentered

PetscDrawStringGetSize

PetscDrawStringSetSize

PetscDrawStringVertical

PetscDrawTensorContour

PetscDrawTensorContourPatch

PetscDrawUtilitySetCmap

PetscDrawUtilitySetGamma

PetscDrawViewFromOptions

PetscDrawViewPortsCreate

PetscDrawViewPortsCreateRect

PetscDrawViewPortsDestroy

PetscDrawViewPortsSet

PetscViewerDrawGetDraw

PetscViewerDrawGetDrawAxis

PetscViewerDrawGetDrawLG

PetscViewerDrawGetDrawType

PetscViewerDrawSetDrawType

PetscXIOErrorHandlerFn

Graphics and Visualization

Viewing Objects (Viewer)

---

## Matlab#

**URL:** https://petsc.org/release/manualpages/Matlab/

**Contents:**
- Matlab#
- No beginner routines#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

Used to interact with Matlab and its Engine

PETSC_MATLAB_ENGINE_SELF

PETSC_MATLAB_ENGINE_WORLD

PetscMatlabEngineCreate

PetscMatlabEngineDestroy

PetscMatlabEngineEvaluate

PetscMatlabEngineGetArray

PetscMatlabEngineGetOutput

PetscMatlabEnginePrintOutput

PetscMatlabEnginePutArray

PETSC_MATLAB_ENGINE_SELF

PETSC_MATLAB_ENGINE_WORLD

PetscMatlabEngineCreate

PetscMatlabEngineDestroy

PetscMatlabEngineEvaluate

PetscMatlabEngineGetArray

PetscMatlabEngineGetOutput

PetscMatlabEnginePrintOutput

PetscMatlabEnginePutArray

---

## PetscBTView#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscBTView/

**Contents:**
- PetscBTView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

View the contents of a PetscBT (bit array) on a PetscViewer, one line per bit

Collective on viewer; No Fortran Support

m - the number of bits in the array to print

viewer - the PetscViewer to print to, or NULL to use PETSC_VIEWER_STDOUT_SELF

PetscBT, PetscBTCreate(), PetscBTLookup(), PetscViewer

src/sys/classes/viewer/utils/btview.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscBTView(PetscCount m, const PetscBT bt, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

---

## PetscDataTypeToHDF5DataType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscDataTypeToHDF5DataType/

**Contents:**
- PetscDataTypeToHDF5DataType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Converts the PETSc name of a datatype to its HDF5 name.

ptype - the PETSc datatype name (for example PETSC_DOUBLE)

htype - the HDF5 datatype

Viewers: Looking at PETSc Objects, PetscDataType, PetscHDF5DataTypeToPetscDataType()

src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewerhdf5.h" 
PetscErrorCode PetscDataTypeToHDF5DataType(PetscDataType ptype, hid_t *htype)
```

Example 2 (unknown):
```unknown
PETSC_DOUBLE
```

Example 3 (unknown):
```unknown
PetscDataType
```

Example 4 (unknown):
```unknown
PetscHDF5DataTypeToPetscDataType()
```

---

## PetscDrawAppendTitle#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAppendTitle/

**Contents:**
- PetscDrawAppendTitle#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the title of a PetscDraw context.

draw - the graphics context

A copy of the string is made, so you may destroy the title string after calling this routine.

PetscDraw, PetscDrawSetTitle(), PetscDrawGetTitle()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawAppendTitle(PetscDraw draw, const char title[])
```

Example 2 (unknown):
```unknown
PetscDrawSetTitle()
```

Example 3 (unknown):
```unknown
PetscDrawGetTitle()
```

---

## PetscDrawArrow#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawArrow/

**Contents:**
- PetscDrawArrow#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a line with arrow head at end if the line is long enough

draw - the drawing context

xl - horizontal coordinate of first end point

yl - vertical coordinate of first end point

xr - horizontal coordinate of second end point

yr - vertical coordinate of second end point

cl - the colors of the endpoints

PetscDraw, PetscDrawLine(), PetscDrawLineSetWidth(), PetscDrawLineGetWidth(), PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawPoint()

src/sys/classes/draw/interface/dline.c

PetscDrawArrow_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawArrow_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawArrow_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawArrow(PetscDraw draw, PetscReal xl, PetscReal yl, PetscReal xr, PetscReal yr, int cl)
```

Example 2 (unknown):
```unknown
PetscDrawLine()
```

Example 3 (unknown):
```unknown
PetscDrawLineSetWidth()
```

Example 4 (unknown):
```unknown
PetscDrawLineGetWidth()
```

---

## PetscDrawAxisCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisCreate/

**Contents:**
- PetscDrawAxisCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Generate the axis data structure.

draw - PetscDraw object where axis to be made

axis - the axis datastructure

The MPI communicator that owns the underlying draw object owns the PetscDrawAxis object, but calls to set PetscDrawAxis options are ignored by all processes except the first MPI rank in the communicator

PetscDrawLGCreate(), PetscDrawLG, PetscDrawSPCreate(), PetscDrawSP, PetscDrawHGCreate(), PetscDrawHG, PetscDrawBarCreate(), PetscDrawBar, PetscDrawLGGetAxis(), PetscDrawSPGetAxis(), PetscDrawHGGetAxis(), PetscDrawBarGetAxis(), PetscDrawAxis, PetscDrawAxisDestroy(), PetscDrawAxisSetColors(), PetscDrawAxisSetLabels(), PetscDrawAxisSetLimits(), PetscDrawAxisGetLimits(), PetscDrawAxisSetHoldLimits(), PetscDrawAxisDraw()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisCreate(PetscDraw draw, PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawAxis
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawAxisDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisDestroy/

**Contents:**
- PetscDrawAxisDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees the space used by an axis structure.

axis - the axis context

PetscDraw, PetscDrawAxisCreate(), PetscDrawAxis

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisDestroy(PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawAxisCreate()
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscDrawAxisDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisDraw/

**Contents:**
- PetscDrawAxisDraw#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

axis - PetscDrawAxis structure

This draws the actual axis. The limits etc have already been set. By picking special routines for the ticks and labels, special effects may be generated. These routines are part of the Axis structure (axis).

PetscDrawAxisCreate(), PetscDrawAxis, PetscDrawAxisGetLimits(), PetscDrawAxisSetLimits(), PetscDrawAxisSetLabels(), PetscDrawAxisSetColors()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisDraw(PetscDrawAxis axis)
```

Example 2 (unknown):
```unknown
PetscDrawAxis
```

Example 3 (unknown):
```unknown
PetscDrawAxisCreate()
```

Example 4 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscDrawAxisGetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisGetLimits/

**Contents:**
- PetscDrawAxisGetLimits#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Gets the limits (in user coords) of the axis

xmin - the lower x limit

xmax - the upper x limit

ymin - the lower y limit

ymax - the upper y limit

PetscDrawAxisCreate(), PetscDrawAxis, PetscDrawAxisSetHoldLimits(), PetscDrawAxisSetLimits(), PetscDrawAxisSetLabels(), PetscDrawAxisSetColors()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisGetLimits(PetscDrawAxis axis, PetscReal *xmin, PetscReal *xmax, PetscReal *ymin, PetscReal *ymax)
```

Example 2 (unknown):
```unknown
PetscDrawAxisCreate()
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawAxisSetHoldLimits()
```

---

## PetscDrawAxisSetColors#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetColors/

**Contents:**
- PetscDrawAxisSetColors#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the colors to be used for the axis, tickmarks, and text.

ac - the color of the axis lines

tc - the color of the tick marks

cc - the color of the text strings

PetscDraw, PetscDrawAxisCreate(), PetscDrawAxis, PetscDrawAxisSetLabels(), PetscDrawAxisDraw(), PetscDrawAxisSetLimits()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisSetColors(PetscDrawAxis axis, int ac, int tc, int cc)
```

Example 2 (unknown):
```unknown
PetscDrawAxisCreate()
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawAxisSetLabels()
```

---

## PetscDrawAxisSetHoldLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetHoldLimits/

**Contents:**
- PetscDrawAxisSetHoldLimits#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Causes an axis to keep the same limits until this is called again

hold - PETSC_TRUE - hold current limits, PETSC_FALSE allow limits to be changed

Once this has been called with PETSC_TRUE the limits will not change if you call PetscDrawAxisSetLimits() until you call this with PETSC_FALSE

PetscDrawAxisCreate(), PetscDrawAxis, PetscDrawAxisGetLimits(), PetscDrawAxisSetLimits(), PetscDrawAxisSetLabels(), PetscDrawAxisSetColors()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisSetHoldLimits(PetscDrawAxis axis, PetscBool hold)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscDrawAxisSetLimits()
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscDrawAxisSetLabels#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetLabels/

**Contents:**
- PetscDrawAxisSetLabels#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the x and y axis labels.

top - the label at the top of the image

xlabel - the x axis label

ylabel - the y axis label

Must be called before PetscDrawAxisDraw() or PetscDrawLGDraw()

There should be no newlines in the arguments

PetscDraw, PetscDrawAxisCreate(), PetscDrawAxis, PetscDrawAxisSetColors(), PetscDrawAxisDraw(), PetscDrawAxisSetLimits()

src/sys/classes/draw/utils/axisc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisSetLabels(PetscDrawAxis axis, const char top[], const char xlabel[], const char ylabel[])
```

Example 2 (unknown):
```unknown
PetscDrawAxisDraw()
```

Example 3 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 4 (unknown):
```unknown
PetscDrawAxisCreate()
```

---

## PetscDrawAxisSetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxisSetLimits/

**Contents:**
- PetscDrawAxisSetLimits#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the limits (in user coords) of the axis

xmin - the lower x limit

xmax - the upper x limit

ymin - the lower y limit

ymax - the upper y limit

-drawaxis_hold - hold the initial set of axis limits for future plotting

PetscDrawAxisSetHoldLimits(), PetscDrawAxisGetLimits(), PetscDrawAxisSetLabels(), PetscDrawAxisSetColors()

src/sys/classes/draw/utils/axisc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawAxisSetLimits(PetscDrawAxis axis, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax)
```

Example 2 (unknown):
```unknown
PetscDrawAxisSetHoldLimits()
```

Example 3 (unknown):
```unknown
PetscDrawAxisGetLimits()
```

Example 4 (unknown):
```unknown
PetscDrawAxisSetLabels()
```

---

## PetscDrawAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawAxis/

**Contents:**
- PetscDrawAxis#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

An object that manages X-Y axis for a PetscDraw

PetscDraw, PetscDrawAxisCreate(), PetscDrawAxisSetLimits(), PetscDrawAxisSetColors(), PetscDrawAxisSetLabels()

include/petscdrawtypes.h

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

_p_PetscDrawAxis in include/petsc/private/drawimpl.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDrawAxis *PetscDrawAxis;
```

Example 2 (unknown):
```unknown
PetscDrawAxisCreate()
```

Example 3 (unknown):
```unknown
PetscDrawAxisSetLimits()
```

Example 4 (unknown):
```unknown
PetscDrawAxisSetColors()
```

---

## PetscDrawBarCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarCreate/

**Contents:**
- PetscDrawBarCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a bar graph data structure.

draw - The window where the graph will be made

bar - The bar graph context

Call PetscDrawBarSetData() to provide the bins to be plotted and then PetscDrawBarDraw() to display the new plot

The difference between a bar chart, PetscDrawBar, and a histogram, PetscDrawHG, is explained here https://stattrek.com/statistics/charts/histogram.aspx?Tutorial=AP

The MPI communicator that owns the PetscDraw owns this PetscDrawBar, but the calls to set options and add data are ignored on all processes except the zeroth MPI process in the communicator. All MPI processes in the communicator must call PetscDrawBarDraw() to display the updated graph.

PetscDrawBar, PetscDrawLGCreate(), PetscDrawLG, PetscDrawSPCreate(), PetscDrawSP, PetscDrawHGCreate(), PetscDrawHG, PetscDrawBarDestroy(), PetscDrawBarSetData(), PetscDrawBarDraw(), PetscDrawBarSave(), PetscDrawBarSetColor(), PetscDrawBarSort(), PetscDrawBarSetLimits(), PetscDrawBarGetAxis(), PetscDrawAxis, PetscDrawBarGetDraw(), PetscDrawBarSetFromOptions()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarCreate(PetscDraw draw, PetscDrawBar *bar)
```

Example 2 (unknown):
```unknown
PetscDrawBarSetData()
```

Example 3 (unknown):
```unknown
PetscDrawBarDraw()
```

Example 4 (unknown):
```unknown
PetscDrawBar
```

---

## PetscDrawBarDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarDestroy/

**Contents:**
- PetscDrawBarDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees all space taken up by bar graph data structure.

bar - The bar graph context

PetscDrawBar, PetscDrawBarCreate()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarDestroy(PetscDrawBar *bar)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

---

## PetscDrawBarDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarDraw/

**Contents:**
- PetscDrawBarDraw#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

bar - The bar graph context

PetscDrawBar, PetscDrawBarCreate(), PetscDrawBarSetData()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarDraw(PetscDrawBar bar)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawBarSetData()
```

---

## PetscDrawBarGetAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarGetAxis/

**Contents:**
- PetscDrawBarGetAxis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the axis context associated with a bar graph. This is useful if one wants to change some axis property, such as labels, color, etc. The axis context should not be destroyed by the application code.

Not Collective, axis is parallel if bar is parallel

bar - The bar graph context

axis - The axis context

PetscDrawBar, PetscDrawBarCreate(), PetscDrawAxis, PetscDrawAxisCreate()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarGetAxis(PetscDrawBar bar, PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscDrawBarGetDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarGetDraw/

**Contents:**
- PetscDrawBarGetDraw#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the draw context associated with a bar graph.

Not Collective, draw is parallel if bar is parallel

bar - The bar graph context

draw - The draw context

PetscDrawBar, PetscDraw, PetscDrawBarCreate(), PetscDrawBarDraw()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarGetDraw(PetscDrawBar bar, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawBarDraw()
```

---

## PetscDrawBarSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSave/

**Contents:**
- PetscDrawBarSave#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Saves a drawn bar graph

bar - The bar graph context

PetscDrawSave(), PetscDrawBar, PetscDrawBarCreate(), PetscDrawBarGetDraw(), PetscDrawSetSave(), PetscDrawBarSetData()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSave(PetscDrawBar bar)
```

Example 2 (unknown):
```unknown
PetscDrawSave()
```

Example 3 (unknown):
```unknown
PetscDrawBar
```

Example 4 (unknown):
```unknown
PetscDrawBarCreate()
```

---

## PetscDrawBarSetColor#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSetColor/

**Contents:**
- PetscDrawBarSetColor#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the color the bars will be drawn with.

bar - The bar graph context

color - one of the colors defined in petscdraw.h or PETSC_DRAW_ROTATE to make each bar a different color

PetscDrawBarCreate(), PetscDrawBar, PetscDrawBarSetData(), PetscDrawBarDraw(), PetscDrawBarGetAxis()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSetColor(PetscDrawBar bar, int color)
```

Example 2 (unknown):
```unknown
PETSC_DRAW_ROTATE
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawBar
```

---

## PetscDrawBarSetData#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSetData/

**Contents:**
- PetscDrawBarSetData#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the data for a bar graph

bar - The bar graph context.

bins - number of items

data - values of each item

labels - optional label for each bar, NULL terminated array of strings

Call PetscDrawBarDraw() after this call to display the new plot

The data is ignored on all MPI processes except rank zero

PetscDrawBar, PetscDrawBarCreate(), PetscDrawBarDraw()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSetData(PetscDrawBar bar, PetscInt bins, const PetscReal data[], const char *const labels[])
```

Example 2 (unknown):
```unknown
PetscDrawBarDraw()
```

Example 3 (unknown):
```unknown
PetscDrawBar
```

Example 4 (unknown):
```unknown
PetscDrawBarCreate()
```

---

## PetscDrawBarSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSetFromOptions/

**Contents:**
- PetscDrawBarSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets options related to the display of the PetscDrawBar

bar - the bar graph context

-bar_sort - sort the entries before drawing the bar graph

Does not set options related to the underlying PetscDraw or PetscDrawAxis

PetscDrawBar, PetscDrawBarDestroy(), PetscDrawBarCreate(), PetscDrawBarSort()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawBar
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSetFromOptions(PetscDrawBar bar)
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawBar
```

---

## PetscDrawBarSetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSetLimits/

**Contents:**
- PetscDrawBarSetLimits#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the axis limits for a bar graph. If more points are added after this call, the limits will be adjusted to include those additional points.

bar - The bar graph context

y_min - The lower limit

y_max - The upper limit

PetscDrawBar, PetscDrawBarCreate(), PetscDrawBarGetAxis(), PetscDrawBarSetData(), PetscDrawBarDraw()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSetLimits(PetscDrawBar bar, PetscReal y_min, PetscReal y_max)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawBarGetAxis()
```

---

## PetscDrawBarSort#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBarSort/

**Contents:**
- PetscDrawBarSort#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sorts the values before drawing the bar chart, the bars will be in ascending order from left to right

bar - The bar graph context

sort - PETSC_TRUE to sort the values

tolerance - discard values less than tolerance

PetscDrawBar, PetscDrawBarCreate(), PetscDrawBarSetData(), PetscDrawBarSetColor(), PetscDrawBarDraw(), PetscDrawBarGetAxis()

src/sys/classes/draw/utils/bars.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawBarSort(PetscDrawBar bar, PetscBool sort, PetscReal tolerance)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawBarCreate()
```

Example 4 (unknown):
```unknown
PetscDrawBarSetData()
```

---

## PetscDrawBar#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBar/

**Contents:**
- PetscDrawBar#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

An object that manages drawing bar graphs

PetscDrawAxis, PetscDraw, PetscDrawLG, PetscDrawHG, PetscDrawSP, PetscDrawBarCreate()

include/petscdrawtypes.h

_p_PetscDrawBar in include/petsc/private/drawimpl.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDrawBar *PetscDrawBar;
```

Example 2 (unknown):
```unknown
PetscDrawAxis
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PetscDrawHG
```

---

## PetscDrawBOP#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawBOP/

**Contents:**
- PetscDrawBOP#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Begins a new page or frame on the selected graphical device.

draw - the drawing context

PetscDrawEOP(), PetscDrawClear()

src/sys/classes/draw/interface/dclear.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawBOP(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawEOP()
```

Example 3 (unknown):
```unknown
PetscDrawClear()
```

---

## PetscDrawButton#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawButton/

**Contents:**
- PetscDrawButton#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Used to determine which button was pressed

PETSC_BUTTON_NONE - no button was pressed

PETSC_BUTTON_LEFT - the left button

PETSC_BUTTON_CENTER - the center button

PETSC_BUTTON_RIGHT - the right button

PETSC_BUTTON_WHEEL_UP - the wheel was moved up

PETSC_BUTTON_WHEEL_DOWN - the wheel was moved down

PETSC_BUTTON_LEFT_SHIFT - the left button and the shift key

PETSC_BUTTON_CENTER_SHIFT- the center button and the shift key

PETSC_BUTTON_RIGHT_SHIFT - the right button and the shift key

PetscDraw, PetscDrawGetMouseButton()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_BUTTON_NONE,
  PETSC_BUTTON_LEFT,
  PETSC_BUTTON_CENTER,
  PETSC_BUTTON_RIGHT,
  PETSC_BUTTON_WHEEL_UP,
  PETSC_BUTTON_WHEEL_DOWN,
  PETSC_BUTTON_LEFT_SHIFT,
  PETSC_BUTTON_CENTER_SHIFT,
  PETSC_BUTTON_RIGHT_SHIFT
} PetscDrawButton;
```

Example 2 (unknown):
```unknown
PETSC_BUTTON_NONE
```

Example 3 (unknown):
```unknown
PETSC_BUTTON_LEFT
```

Example 4 (unknown):
```unknown
PETSC_BUTTON_CENTER
```

---

## PetscDrawCheckResizedWindow#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawCheckResizedWindow/

**Contents:**
- PetscDrawCheckResizedWindow#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Checks if the user has resized the window.

PetscDraw, PetscDrawResizeWindow()

src/sys/classes/draw/interface/draw.c

PetscDrawCheckResizedWindow_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawCheckResizedWindow_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawCheckResizedWindow_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawCheckResizedWindow(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawResizeWindow()
```

---

## PetscDrawClear#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawClear/

**Contents:**
- PetscDrawClear#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Clears graphical output. All processors must call this routine. Does not return until the draw in context is clear.

draw - the drawing context

PetscDrawBOP(), PetscDrawEOP()

src/sys/classes/draw/interface/dclear.c

PetscDrawClear_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawClear_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawClear_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawClear_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawClear(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawBOP()
```

Example 3 (unknown):
```unknown
PetscDrawEOP()
```

---

## PetscDrawCollectiveBegin#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawCollectiveBegin/

**Contents:**
- PetscDrawCollectiveBegin#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Begins a set of draw operations Collective

draw - the draw object

This is a macro that handles its own error checking, it does not return an error code.

The set of operations needs to be ended by a call to PetscDrawCollectiveEnd().

X windows draw operations that are enclosed by these routines handle correctly resizing or closing of the window without crashing the program.

This only applies to X windows and so should have a more specific name such as PetscDrawXCollectiveBegin()

PetscDraw, PetscDrawCollectiveEnd()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscdraw.h>
PetscErrorCode PetscDrawCollectiveBegin(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawCollectiveEnd()
```

Example 3 (unknown):
```unknown
PetscDrawXCollectiveBegin()
```

Example 4 (unknown):
```unknown
PetscDrawCollectiveEnd()
```

---

## PetscDrawCollectiveEnd#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawCollectiveEnd/

**Contents:**
- PetscDrawCollectiveEnd#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Ends a set of draw operations begun with PetscDrawCollectiveBegin() Collective

draw - the draw object

This is a macro that handles its own error checking, it does not return an error code.

X windows draw operations that are enclosed by these routines handle correctly resizing or closing of the window without crashing the program.

This only applies to X windows and so should have a more specific name such as PetscDrawXCollectiveEnd()

PetscDraw, PetscDrawCollectiveBegin()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawCollectiveBegin()
```

Example 2 (cpp):
```cpp
#include <petscdraw.h>
PetscErrorCode PetscDrawCollectiveEnd(PetscDraw draw)
```

Example 3 (unknown):
```unknown
PetscDrawXCollectiveEnd()
```

Example 4 (unknown):
```unknown
PetscDrawCollectiveBegin()
```

---

## PetscDrawCoordinateToPixel#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawCoordinateToPixel/

**Contents:**
- PetscDrawCoordinateToPixel#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

given a coordinate in a PetscDraw returns the pixel location

draw - the draw where the coordinates are defined

x - the horizontal coordinate

y - the vertical coordinate

i - the horizontal pixel location

j - the vertical pixel location

src/sys/classes/draw/interface/drect.c

PetscDrawCoordinateToPixel_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawCoordinateToPixel_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawCoordinateToPixel_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawCoordinateToPixel(PetscDraw draw, PetscReal x, PetscReal y, int *i, int *j)
```

---

## PetscDrawCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawCreate/

**Contents:**
- PetscDrawCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a graphics context.

comm - MPI communicator

display - X display when using X Windows

title - optional title added to top of window

x - horizonatl coordinate of lower left corner of window or PETSC_DECIDE

y - vertical coordinate of lower left corner of window or PETSC_DECIDE

w - width of window, PETSC_DECIDE, PETSC_DRAW_HALF_SIZE, PETSC_DRAW_FULL_SIZE, PETSC_DRAW_THIRD_SIZE or PETSC_DRAW_QUARTER_SIZE

h - height of window, PETSC_DECIDE, PETSC_DRAW_HALF_SIZE, PETSC_DRAW_FULL_SIZE, PETSC_DRAW_THIRD_SIZE or PETSC_DRAW_QUARTER_SIZE

indraw - location to put the PetscDraw context

PetscDrawSetType(), PetscDrawSetFromOptions(), PetscDrawDestroy(), PetscDrawLGCreate(), PetscDrawSPCreate(), PetscDrawViewPortsCreate(), PetscDrawViewPortsSet(), PetscDrawAxisCreate(), PetscDrawHGCreate(), PetscDrawBarCreate(), PetscViewerDrawGetDraw(), PetscDrawSetSave(), PetscDrawSetSaveMovie(), PetscDrawSetSaveFinalImage(), PetscDrawOpenX(), PetscDrawOpenImage(), PetscDrawIsNull(), PetscDrawGetPopup(), PetscDrawCheckResizedWindow(), PetscDrawResizeWindow(), PetscDrawGetWindowSize(), PetscDrawLine(), PetscDrawArrow(), PetscDrawLineSetWidth(), PetscDrawLineGetWidth(), PetscDrawMarker(), PetscDrawPoint(), PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawString(), PetscDrawStringCentered(), PetscDrawStringBoxed(), PetscDrawStringVertical(), PetscDrawSetViewPort(), PetscDrawGetViewPort(), PetscDrawSplitViewPort(), PetscDrawSetTitle(), PetscDrawAppendTitle(), PetscDrawGetTitle(), PetscDrawSetPause(), PetscDrawGetPause(), PetscDrawPause(), PetscDrawSetDoubleBuffer(), PetscDrawClear(), PetscDrawFlush(), PetscDrawGetSingleton(), PetscDrawGetMouseButton(), PetscDrawZoom(), PetscDrawGetBoundingBox()

src/sys/classes/draw/interface/drawreg.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

PetscDrawCreate_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawCreate_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawCreate_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawCreate_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawCreate_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawCreate(MPI_Comm comm, const char display[], const char title[], int x, int y, int w, int h, PetscDraw *indraw)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## PetscDrawDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawDestroy/

**Contents:**
- PetscDrawDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Deletes a draw context.

draw - the drawing context

PetscDraw, PetscDrawCreate()

src/sys/classes/draw/interface/draw.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

PetscDrawDestroy_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawDestroy_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawDestroy_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawDestroy_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawDestroy(PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawEllipse#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawEllipse/

**Contents:**
- PetscDrawEllipse#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Draws an ellipse onto a drawable.

draw - The drawing context

x - The x coordinate of the center

y - The y coordinate of the center

a - The major axes length

b - The minor axes length

PetscDraw, PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawMarker(), PetscDrawPoint(), PetscDrawString(), PetscDrawArrow()

src/sys/classes/draw/interface/dellipse.c

PetscDrawEllipse_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawEllipse_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawEllipse_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawEllipse_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawEllipse(PetscDraw draw, PetscReal x, PetscReal y, PetscReal a, PetscReal b, int c)
```

Example 2 (unknown):
```unknown
PetscDrawRectangle()
```

Example 3 (unknown):
```unknown
PetscDrawTriangle()
```

Example 4 (unknown):
```unknown
PetscDrawMarker()
```

---

## PetscDrawEOP#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawEOP/

**Contents:**
- PetscDrawEOP#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Ends a page or frame on the selected graphical device.

draw - the drawing context

PetscDrawBOP(), PetscDrawClear()

src/sys/classes/draw/interface/dclear.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawEOP(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawBOP()
```

Example 3 (unknown):
```unknown
PetscDrawClear()
```

---

## PetscDrawFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawFinalizePackage/

**Contents:**
- PetscDrawFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc interface to the PetscDraw package. It is called from PetscFinalize().

PetscDraw, PetscFinalize()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## PetscDrawFlush#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawFlush/

**Contents:**
- PetscDrawFlush#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Flushes graphical output.

draw - the drawing context

PetscDraw, PetscDrawClear()

src/sys/classes/draw/interface/dflush.c

PetscDrawFlush_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawFlush_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawFlush_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawFlush(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawClear()
```

---

## PetscDrawGetBoundingBox#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetBoundingBox/

**Contents:**
- PetscDrawGetBoundingBox#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the bounding box of all PetscDrawStringBoxed() commands

draw - the drawing context

xl - horizontal coordinate of lower left corner of bounding box

yl - vertical coordinate of lower left corner of bounding box

xr - horizontal coordinate of upper right corner of bounding box

yr - vertical coordinate of upper right corner of bounding box

PetscDraw, PetscDrawPushCurrentPoint(), PetscDrawPopCurrentPoint(), PetscDrawSetCurrentPoint()

src/sys/classes/draw/interface/dline.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawStringBoxed()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetBoundingBox(PetscDraw draw, PetscReal *xl, PetscReal *yl, PetscReal *xr, PetscReal *yr)
```

Example 3 (unknown):
```unknown
PetscDrawPushCurrentPoint()
```

Example 4 (unknown):
```unknown
PetscDrawPopCurrentPoint()
```

---

## PetscDrawGetCoordinates#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetCoordinates/

**Contents:**
- PetscDrawGetCoordinates#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the application coordinates of the corners of the window (or page).

draw - the drawing object

xl - the horizontal coordinate of the lower left corner of the drawing region.

yl - the vertical coordinate of the lower left corner of the drawing region.

xr - the horizontal coordinate of the upper right corner of the drawing region.

yr - the vertical coordinate of the upper right corner of the drawing region.

PetscDraw, PetscDrawSetCoordinates()

src/sys/classes/draw/interface/dcoor.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetCoordinates(PetscDraw draw, PetscReal *xl, PetscReal *yl, PetscReal *xr, PetscReal *yr)
```

Example 2 (unknown):
```unknown
PetscDrawSetCoordinates()
```

---

## PetscDrawGetCurrentPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetCurrentPoint/

**Contents:**
- PetscDrawGetCurrentPoint#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the current draw point, some codes use this point to determine where to draw next

draw - the drawing context

x - horizontal coordinate of the current point

y - vertical coordinate of the current point

PetscDraw, PetscDrawPushCurrentPoint(), PetscDrawPopCurrentPoint(), PetscDrawSetCurrentPoint()

src/sys/classes/draw/interface/dline.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetCurrentPoint(PetscDraw draw, PetscReal *x, PetscReal *y)
```

Example 2 (unknown):
```unknown
PetscDrawPushCurrentPoint()
```

Example 3 (unknown):
```unknown
PetscDrawPopCurrentPoint()
```

Example 4 (unknown):
```unknown
PetscDrawSetCurrentPoint()
```

---

## PetscDrawGetMarkerType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetMarkerType/

**Contents:**
- PetscDrawGetMarkerType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

gets the type of marker to display with PetscDrawMarker()

draw - the drawing context

mtype - either PETSC_DRAW_MARKER_CROSS (default) or PETSC_DRAW_MARKER_POINT

PetscDraw, PetscDrawPoint(), PetscDrawMarker(), PetscDrawSetMarkerType(), PetscDrawMarkerType

src/sys/classes/draw/interface/dmarker.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawMarker()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetMarkerType(PetscDraw draw, PetscDrawMarkerType *mtype)
```

Example 3 (unknown):
```unknown
PETSC_DRAW_MARKER_CROSS
```

Example 4 (unknown):
```unknown
PETSC_DRAW_MARKER_POINT
```

---

## PetscDrawGetMouseButton#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetMouseButton/

**Contents:**
- PetscDrawGetMouseButton#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Returns location of mouse and which button was pressed. Waits for button to be pressed.

draw - the window to be used

button - one of PETSC_BUTTON_LEFT, PETSC_BUTTON_CENTER, PETSC_BUTTON_RIGHT, PETSC_BUTTON_WHEEL_UP, PETSC_BUTTON_WHEEL_DOWN

x_user - horizontal user coordinate of location (user may pass in NULL).

y_user - vertical user coordinate of location (user may pass in NULL).

x_phys - horizontal window coordinate (user may pass in NULL).

y_phys - vertical window coordinate (user may pass in NULL).

Only processor 0 actually waits for the button to be pressed.

PetscDraw, PetscDrawButton

src/sys/classes/draw/interface/dmouse.c

PetscDrawGetMouseButton_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawGetMouseButton_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawGetMouseButton_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetMouseButton(PetscDraw draw, PetscDrawButton *button, PetscReal *x_user, PetscReal *y_user, PetscReal *x_phys, PetscReal *y_phys)
```

Example 2 (unknown):
```unknown
PETSC_BUTTON_LEFT
```

Example 3 (unknown):
```unknown
PETSC_BUTTON_CENTER
```

Example 4 (unknown):
```unknown
PETSC_BUTTON_RIGHT
```

---

## PetscDrawGetPause#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetPause/

**Contents:**
- PetscDrawGetPause#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the amount of time that program pauses after a PetscDrawPause() is called.

draw - the drawing object

lpause - number of seconds to pause, -1 implies until user input

By default the pause time is zero unless the -draw_pause option is given

PetscDraw, PetscDrawSetPause(), PetscDrawPause()

src/sys/classes/draw/interface/dpause.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawPause()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetPause(PetscDraw draw, PetscReal *lpause)
```

Example 3 (unknown):
```unknown
PetscDrawSetPause()
```

Example 4 (unknown):
```unknown
PetscDrawPause()
```

---

## PetscDrawGetPopup#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetPopup/

**Contents:**
- PetscDrawGetPopup#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a popup window associated with a PetscDraw window.

draw - the original window

popup - the new popup window

PetscDraw, PetscDrawScalePopup(), PetscDrawCreate()

src/sys/classes/draw/interface/draw.c

PetscDrawGetPopup_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawGetPopup_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawGetPopup_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetPopup(PetscDraw draw, PetscDraw *popup)
```

Example 2 (unknown):
```unknown
PetscDrawScalePopup()
```

Example 3 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawGetSingleton#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetSingleton/

**Contents:**
- PetscDrawGetSingleton#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gain access to a PetscDraw object as if it were owned by the one process.

draw - the original window

sdraw - the singleton window

PetscDraw, PetscDrawRestoreSingleton(), PetscViewerGetSingleton(), PetscViewerRestoreSingleton()

src/sys/classes/draw/interface/draw.c

PetscDrawGetSingleton_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawGetSingleton_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawGetSingleton_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetSingleton(PetscDraw draw, PetscDraw *sdraw)
```

Example 2 (unknown):
```unknown
PetscDrawRestoreSingleton()
```

Example 3 (unknown):
```unknown
PetscViewerGetSingleton()
```

Example 4 (unknown):
```unknown
PetscViewerRestoreSingleton()
```

---

## PetscDrawGetTitle#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetTitle/

**Contents:**
- PetscDrawGetTitle#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets pointer to title of a PetscDraw context.

draw - the graphics context

PetscDraw, PetscDrawSetTitle()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetTitle(PetscDraw draw, const char *title[])
```

Example 2 (unknown):
```unknown
PetscDrawSetTitle()
```

---

## PetscDrawGetType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetType/

**Contents:**
- PetscDrawGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the PetscDraw type as a string from the PetscDraw object.

draw - Krylov context

type - name of PetscDraw method

type should not be retained for later use as it will be an invalid pointer if the PetscDrawType of draw is changed.

PetscDraw, PetscDrawType, PetscDrawSetType(), PetscDrawCreate(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/sys/classes/draw/interface/drawreg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawGetType(PetscDraw draw, PetscDrawType *type)
```

Example 2 (unknown):
```unknown
PetscDrawType
```

Example 3 (unknown):
```unknown
PetscDrawType
```

Example 4 (unknown):
```unknown
PetscDrawSetType()
```

---

## PetscDrawGetViewPort#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetViewPort/

**Contents:**
- PetscDrawGetViewPort#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets the portion of the window (page) to which draw routines will write.

draw - the drawing context

xl - the horizontal coordinate of the lower left corner of the subwindow.

yl - the vertical coordinate of the lower left corner of the subwindow.

xr - the horizontal coordinate of the upper right corner of the subwindow.

yr - the vertical coordinate of the upper right corner of the subwindow.

These numbers must always be between 0.0 and 1.0.

Lower left corner is (0,0).

PetscDraw, PetscDrawSplitViewPort(), PetscDrawSetViewPort()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetViewPort(PetscDraw draw, PetscReal *xl, PetscReal *yl, PetscReal *xr, PetscReal *yr)
```

Example 2 (unknown):
```unknown
PetscDrawSplitViewPort()
```

Example 3 (unknown):
```unknown
PetscDrawSetViewPort()
```

---

## PetscDrawGetWindowSize#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawGetWindowSize/

**Contents:**
- PetscDrawGetWindowSize#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the size of the window.

h - the window height

PetscDraw, PetscDrawResizeWindow(), PetscDrawCheckResizedWindow()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawGetWindowSize(PetscDraw draw, int *w, int *h)
```

Example 2 (unknown):
```unknown
PetscDrawResizeWindow()
```

Example 3 (unknown):
```unknown
PetscDrawCheckResizedWindow()
```

---

## PetscDrawHGAddValue#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGAddValue/

**Contents:**
- PetscDrawHGAddValue#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds another value to the histogram.

Calls to this function are used to create a standard histogram with integer bin heights. Use calls to PetscDrawHGAddWeightedValue() to create a histogram with non-integer bin heights.

PetscDrawHGCreate(), PetscDrawHG, PetscDrawHGDraw(), PetscDrawHGReset(), PetscDrawHGAddWeightedValue()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGAddValue(PetscDrawHG hist, PetscReal value)
```

Example 2 (unknown):
```unknown
PetscDrawHGAddWeightedValue()
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHG
```

---

## PetscDrawHGAddWeightedValue#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGAddWeightedValue/

**Contents:**
- PetscDrawHGAddWeightedValue#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Adds another value to the histogram with a weight.

weight - The value weight

Calls to this function are used to create a histogram with non-integer bin heights. Use calls to PetscDrawHGAddValue() to create a standard histogram with integer bin heights.

This allows us to histogram frequency and probability distributions (https://learnche.org/pid/univariate-review/histograms-and-probability-distributions). We can use this to look at particle weight distributions in Particle-in-Cell (PIC) methods, for example.

PetscDrawHGCreate(), PetscDrawHG, PetscDrawHGDraw(), PetscDrawHGReset(), PetscDrawHGAddValue()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGAddWeightedValue(PetscDrawHG hist, PetscReal value, PetscReal weight)
```

Example 2 (unknown):
```unknown
PetscDrawHGAddValue()
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHG
```

---

## PetscDrawHGCalcStats#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGCalcStats/

**Contents:**
- PetscDrawHGCalcStats#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Turns on calculation of descriptive statistics associated with the histogram

hist - The histogram context

calc - Flag for calculation

PetscDrawHG, PetscDrawHGCreate(), PetscDrawHGAddValue(), PetscDrawHGView(), PetscDrawHGDraw()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGCalcStats(PetscDrawHG hist, PetscBool calc)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHGAddValue()
```

---

## PetscDrawHGCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGCreate/

**Contents:**
- PetscDrawHGCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a histogram data structure.

draw - The window where the graph will be made

bins - The number of bins to use

hist - The histogram context

The difference between a bar chart, PetscDrawBar, and a histogram, PetscDrawHG, is explained here https://stattrek.com/statistics/charts/histogram.aspx?Tutorial=AP

The histogram is only displayed when PetscDrawHGDraw() is called.

The MPI communicator that owns the PetscDraw owns this PetscDrawHG, but the calls to set options and add data are ignored on all processes except the zeroth MPI process in the communicator. All MPI processes in the communicator must call PetscDrawHGDraw() to display the updated graph.

PetscDrawHGDestroy(), PetscDrawHG, PetscDrawBarCreate(), PetscDrawBar, PetscDrawLGCreate(), PetscDrawLG, PetscDrawSPCreate(), PetscDrawSP, PetscDrawHGSetNumberBins(), PetscDrawHGReset(), PetscDrawHGAddValue(), PetscDrawHGDraw(), PetscDrawHGSave(), PetscDrawHGView(), PetscDrawHGSetColor(), PetscDrawHGSetLimits(), PetscDrawHGCalcStats(), PetscDrawHGIntegerBins(), PetscDrawHGGetAxis(), PetscDrawAxis, PetscDrawHGGetDraw()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGCreate(PetscDraw draw, int bins, PetscDrawHG *hist)
```

Example 2 (unknown):
```unknown
PetscDrawBar
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

Example 4 (unknown):
```unknown
PetscDrawHGDraw()
```

---

## PetscDrawHGDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGDestroy/

**Contents:**
- PetscDrawHGDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees all space taken up by histogram data structure.

hist - The histogram context

PetscDrawHGCreate(), PetscDrawHG

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGDestroy(PetscDrawHG *hist)
```

Example 2 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

---

## PetscDrawHGDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGDraw/

**Contents:**
- PetscDrawHGDraw#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

hist - The histogram context

PetscDrawHGCreate(), PetscDrawHG, PetscDrawHGAddValue(), PetscDrawHGReset()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGDraw(PetscDrawHG hist)
```

Example 2 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

Example 4 (unknown):
```unknown
PetscDrawHGAddValue()
```

---

## PetscDrawHGGetAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGGetAxis/

**Contents:**
- PetscDrawHGGetAxis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the axis context associated with a histogram. This is useful if one wants to change some axis property, such as labels, color, etc. The axis context should not be destroyed by the application code.

Not Collective, axis is parallel if hist is parallel

hist - The histogram context

axis - The axis context

PetscDrawHG, PetscDrawAxis, PetscDrawHGCreate(), PetscDrawHGAddValue(), PetscDrawHGView(), PetscDrawHGDraw(), PetscDrawHGSetColor(), PetscDrawHGSetLimits()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGGetAxis(PetscDrawHG hist, PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawHGCreate()
```

---

## PetscDrawHGGetDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGGetDraw/

**Contents:**
- PetscDrawHGGetDraw#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the draw context associated with a histogram.

Not Collective, draw is parallel if hist is parallel

hist - The histogram context

draw - The draw context

PetscDraw, PetscDrawHG, PetscDrawHGCreate(), PetscDrawHGAddValue(), PetscDrawHGView(), PetscDrawHGDraw(), PetscDrawHGSetColor(), PetscDrawAxis, PetscDrawHGSetLimits()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGGetDraw(PetscDrawHG hist, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHGAddValue()
```

---

## PetscDrawHGIntegerBins#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGIntegerBins/

**Contents:**
- PetscDrawHGIntegerBins#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Turns on integer width bins

hist - The histogram context

ints - Flag for integer width bins

PetscDrawHG, PetscDrawHGCreate(), PetscDrawHGAddValue(), PetscDrawHGView(), PetscDrawHGDraw(), PetscDrawHGSetColor()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGIntegerBins(PetscDrawHG hist, PetscBool ints)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHGAddValue()
```

---

## PetscDrawHGReset#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGReset/

**Contents:**
- PetscDrawHGReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears histogram to allow for reuse with new data.

hist - The histogram context.

PetscDrawHGCreate(), PetscDrawHG, PetscDrawHGDraw(), PetscDrawHGAddValue()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGReset(PetscDrawHG hist)
```

Example 2 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

Example 4 (unknown):
```unknown
PetscDrawHGDraw()
```

---

## PetscDrawHGSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGSave/

**Contents:**
- PetscDrawHGSave#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

hg - The histogram context

PetscDrawSave(), PetscDrawHGCreate(), PetscDrawHGGetDraw(), PetscDrawSetSave(), PetscDrawHGDraw()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGSave(PetscDrawHG hg)
```

Example 2 (unknown):
```unknown
PetscDrawSave()
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHGGetDraw()
```

---

## PetscDrawHGSetColor#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGSetColor/

**Contents:**
- PetscDrawHGSetColor#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the color the bars will be drawn with.

hist - The histogram context

color - one of the colors defined in petscdraw.h or PETSC_DRAW_ROTATE to make each bar a different color

PetscDrawHG, PetscDrawHGCreate(), PetscDrawHGGetDraw(), PetscDrawSetSave(), PetscDrawSave(), PetscDrawHGDraw(), PetscDrawHGGetAxis()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGSetColor(PetscDrawHG hist, int color)
```

Example 2 (unknown):
```unknown
PETSC_DRAW_ROTATE
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

Example 4 (unknown):
```unknown
PetscDrawHGCreate()
```

---

## PetscDrawHGSetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGSetLimits/

**Contents:**
- PetscDrawHGSetLimits#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the axis limits for a histogram. If more points are added after this call, the limits will be adjusted to include those additional points.

hist - The histogram context

x_min - the horizontal lower limit

x_max - the horizontal upper limit

y_min - the vertical lower limit

y_max - the vertical upper limit

PetscDrawHG, PetscDrawHGCreate(), PetscDrawHGGetDraw(), PetscDrawSetSave(), PetscDrawSave(), PetscDrawHGDraw(), PetscDrawHGGetAxis()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGSetLimits(PetscDrawHG hist, PetscReal x_min, PetscReal x_max, int y_min, int y_max)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawHGGetDraw()
```

---

## PetscDrawHGSetNumberBins#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGSetNumberBins/

**Contents:**
- PetscDrawHGSetNumberBins#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Change the number of bins that are to be drawn in the histogram

hist - The histogram context.

bins - The number of bins.

PetscDrawHGCreate(), PetscDrawHG, PetscDrawHGDraw(), PetscDrawHGIntegerBins()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGSetNumberBins(PetscDrawHG hist, int bins)
```

Example 2 (unknown):
```unknown
PetscDrawHGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawHG
```

Example 4 (unknown):
```unknown
PetscDrawHGDraw()
```

---

## PetscDrawHGView#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHGView/

**Contents:**
- PetscDrawHGView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Prints the histogram information to a viewer

hist - The histogram context

viewer - The viewer to view it with

PetscDrawHG, PetscViewer, PetscDrawHGCreate(), PetscDrawHGGetDraw(), PetscDrawSetSave(), PetscDrawSave(), PetscDrawHGDraw()

src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawHGView(PetscDrawHG hist, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscDrawHG
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscDrawHGCreate()
```

---

## PetscDrawHG#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawHG/

**Contents:**
- PetscDrawHG#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

An object that manages drawing histograms

Use a series of calls to PetscDrawHGAddValue() to create a standard histogram https://en.wikipedia.org/wiki/Histogram, where the bins have integer counts. Use calls to PetscDrawHGAddWeightedValue() to create a histogram with non-integer bin heights, such as the following https://mathematica.stackexchange.com/questions/103928/histogram-from-relative-frequency-data

PetscDrawAxis, PetscDraw, PetscDrawLG, PetscDrawBar, PetscDrawSP, PetscDrawHGCreate(), PetscDrawHGAddValue(), PetscDrawHGAddWeightedValue()

include/petscdrawtypes.h

_p_PetscDrawHG in src/sys/classes/draw/utils/hists.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDrawHG *PetscDrawHG;
```

Example 2 (unknown):
```unknown
PetscDrawHGAddValue()
```

Example 3 (unknown):
```unknown
PetscDrawHGAddWeightedValue()
```

Example 4 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscDrawIndicatorFunction#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawIndicatorFunction/

**Contents:**
- PetscDrawIndicatorFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Draws an indicator function (where a relationship is true) on a PetscDraw

xmin - region to draw indicator function

xmax - region to draw indicator function

ymin - region to draw indicator function

ymax - region to draw indicator function

c - the color of the region

indicator - the indicator function

ctx - the context to pass to the indicator function

src/sys/classes/draw/interface/drect.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawIndicatorFunction(PetscDraw draw, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax, int c, PetscErrorCode (*indicator)(PetscCtx, PetscReal, PetscReal, PetscBool *), PetscCtx ctx)
```

---

## PetscDrawInitializePackage#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawInitializePackage/

**Contents:**
- PetscDrawInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscDraw package. It is called from PetscDLLibraryRegister_petsc() when using dynamic libraries, and on the call to PetscInitialize() when using shared or static libraries.

PetscDraw, PetscInitialize()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscInitialize()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## PetscDrawIsNull#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawIsNull/

**Contents:**
- PetscDrawIsNull#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns PETSC_TRUE if draw is a null draw object.

draw - the draw context

yes - PETSC_TRUE if it is a null draw object; otherwise PETSC_FALSE

PetscDraw, PETSC_DRAW_NULL, PetscDrawOpenX()

src/sys/classes/draw/impls/null/drawnull.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawIsNull(PetscDraw draw, PetscBool *yes)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PETSC_DRAW_NULL
```

Example 4 (unknown):
```unknown
PetscDrawOpenX()
```

---

## PetscDrawLGAddCommonPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGAddCommonPoint/

**Contents:**
- PetscDrawLGAddCommonPoint#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Adds another point to each of the line graphs. All the points share the same new X coordinate. The new point must have an X coordinate larger than the old points.

lg - the line graph context

x - the common x coordinate point

y - the new y coordinate point for each curve.

You must call PetscDrawLGDraw() to display any added points

Call PetscDrawLGReset() to remove all points

PetscDrawLG, PetscDrawLGCreate(), PetscDrawLGAddPoints(), PetscDrawLGAddPoint(), PetscDrawLGReset(), PetscDrawLGDraw()

src/sys/classes/draw/utils/lg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGAddCommonPoint(PetscDrawLG lg, const PetscReal x, const PetscReal *y)
```

Example 2 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 3 (unknown):
```unknown
PetscDrawLGReset()
```

Example 4 (unknown):
```unknown
PetscDrawLG
```

---

## PetscDrawLGAddPoints#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGAddPoints/

**Contents:**
- PetscDrawLGAddPoints#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Adds several points to each of the line graphs. The new points must have an X coordinate larger than the old points.

lg - the line graph context

xx - array of pointers that point to arrays containing the new x coordinates for each curve.

yy - array of pointers that point to arrays containing the new y points for each curve.

n - number of points being added

You must call PetscDrawLGDraw() to display any added points

Call PetscDrawLGReset() to remove all points

PetscDrawLG, PetscDrawLGCreate(), PetscDrawLGAddPoint(), PetscDrawLGAddCommonPoint(), PetscDrawLGReset(), PetscDrawLGDraw()

src/sys/classes/draw/utils/lg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGAddPoints(PetscDrawLG lg, PetscInt n, PetscReal *xx[], PetscReal *yy[])
```

Example 2 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 3 (unknown):
```unknown
PetscDrawLGReset()
```

Example 4 (unknown):
```unknown
PetscDrawLG
```

---

## PetscDrawLGAddPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGAddPoint/

**Contents:**
- PetscDrawLGAddPoint#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Adds another point to each of the line graphs. The new point must have an X coordinate larger than the old points.

lg - the line graph context

x - array containing the x coordinate for the point on each curve

y - array containing the y coordinate for the point on each curve

You must call PetscDrawLGDraw() to display any added points

Call PetscDrawLGReset() to remove all points

PetscDrawLG, PetscDrawLGCreate(), PetscDrawLGAddPoints(), PetscDrawLGAddCommonPoint(), PetscDrawLGReset(), PetscDrawLGDraw()

src/sys/classes/draw/utils/lg.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGAddPoint(PetscDrawLG lg, const PetscReal *x, const PetscReal *y)
```

Example 2 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 3 (unknown):
```unknown
PetscDrawLGReset()
```

Example 4 (unknown):
```unknown
PetscDrawLG
```

---

## PetscDrawLGCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGCreate/

**Contents:**
- PetscDrawLGCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a line graph data structure.

draw - the window where the graph will be made.

dim - the number of curves which will be drawn

outlg - the line graph context

The MPI communicator that owns the PetscDraw owns this PetscDrawLG, but the calls to set options and add points are ignored on all processes except the zeroth MPI process in the communicator.

All MPI ranks in the communicator must call PetscDrawLGDraw() to display the updated graph.

PetscDrawLGDestroy(), PetscDrawLGAddPoint(), PetscDrawLGAddCommonPoint(), PetscDrawLGAddPoints(), PetscDrawLGDraw(), PetscDrawLGSave(), PetscDrawLGView(), PetscDrawLGReset(), PetscDrawLGSetDimension(), PetscDrawLGGetDimension(), PetscDrawLGSetLegend(), PetscDrawLGGetAxis(), PetscDrawLGGetDraw(), PetscDrawLGSetUseMarkers(), PetscDrawLGSetLimits(), PetscDrawLGSetColors(), PetscDrawLGSetOptionsPrefix(), PetscDrawLGSetFromOptions()

src/sys/classes/draw/utils/lgc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGCreate(PetscDraw draw, PetscInt dim, PetscDrawLG *outlg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 4 (unknown):
```unknown
PetscDrawLGDestroy()
```

---

## PetscDrawLGDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGDestroy/

**Contents:**
- PetscDrawLGDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Frees all space taken up by line graph data structure.

lg - the line graph context

PetscDrawLG, PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGDestroy(PetscDrawLG *lg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGDraw/

**Contents:**
- PetscDrawLGDraw#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Redraws a line graph.

lg - the line graph context

PetscDrawLG, PetscDrawSPDraw(), PetscDrawLGSPDraw(), PetscDrawLGReset()

src/sys/classes/draw/utils/lgc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGDraw(PetscDrawLG lg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawSPDraw()
```

Example 4 (unknown):
```unknown
PetscDrawLGSPDraw()
```

---

## PetscDrawLGGetAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGGetAxis/

**Contents:**
- PetscDrawLGGetAxis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the axis context associated with a line graph. This is useful if one wants to change some axis property, such as labels, color, etc. The axis context should not be destroyed by the application code.

Not Collective, if lg is parallel then axis is parallel

lg - the line graph context

axis - the axis context

PetscDrawLGCreate(), PetscDrawAxis, PetscDrawLG

src/sys/classes/draw/utils/lgc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGGetAxis(PetscDrawLG lg, PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawLG
```

---

## PetscDrawLGGetData#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGGetData/

**Contents:**
- PetscDrawLGGetData#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the data being plotted.

lg - the line graph context

dim - the number of curves

n - the number of points on each line

x - The x-value of each point, x[p * dim + c]

y - The y-value of each point, y[p * dim + c]

PetscDrawLGC, PetscDrawLGCreate(), PetscDrawLGGetDimension()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGGetData(PetscDrawLG lg, PetscInt *dim, PetscInt *n, const PetscReal *x[], const PetscReal *y[])
```

Example 2 (unknown):
```unknown
PetscDrawLGC
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawLGGetDimension()
```

---

## PetscDrawLGGetDimension#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGGetDimension/

**Contents:**
- PetscDrawLGGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of curves that are to be drawn.

lg - the line graph context.

dim - the number of curves.

PetscDrawLGC, PetscDrawLGCreate(), PetscDrawLGSetDimension()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGGetDimension(PetscDrawLG lg, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscDrawLGC
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 4 (unknown):
```unknown
PetscDrawLGSetDimension()
```

---

## PetscDrawLGGetDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGGetDraw/

**Contents:**
- PetscDrawLGGetDraw#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the draw context associated with a line graph.

Not Collective, if lg is parallel then draw is parallel

lg - the line graph context

draw - the draw context

PetscDrawLGCreate(), PetscDraw, PetscDrawLG

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGGetDraw(PetscDrawLG lg, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

---

## PetscDrawLGReset#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGReset/

**Contents:**
- PetscDrawLGReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears line graph to allow for reuse with new data.

lg - the line graph context.

PetscDrawLG, PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGReset(PetscDrawLG lg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSave/

**Contents:**
- PetscDrawLGSave#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

lg - The line graph context

PetscDrawLG, PetscDrawSave(), PetscDrawLGCreate(), PetscDrawLGGetDraw(), PetscDrawSetSave()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSave(PetscDrawLG lg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawSave()
```

Example 4 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGSetColors#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetColors/

**Contents:**
- PetscDrawLGSetColors#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the color of each line graph drawn

lg - the line graph context.

colors - the colors, an array of length the value set with PetscDrawLGSetDimension()

PetscDrawLG, PetscDrawLGCreate(), PetscDrawLGSetDimension(), PetscDrawLGGetDimension()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetColors(PetscDrawLG lg, const int colors[])
```

Example 2 (unknown):
```unknown
PetscDrawLGSetDimension()
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGSetDimension#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetDimension/

**Contents:**
- PetscDrawLGSetDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Change the number of curves that are to be drawn.

lg - the line graph context.

dim - the number of curves.

PetscDrawLGCreate(), PetscDrawLGGetDimension()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetDimension(PetscDrawLG lg, PetscInt dim)
```

Example 2 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawLGGetDimension()
```

---

## PetscDrawLGSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetFromOptions/

**Contents:**
- PetscDrawLGSetFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets options related to the line graph object

lg - the line graph context

-lg_use_markers (true|false) - true means it draws a marker for each point

PetscDrawLG, PetscDrawLGDestroy(), PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetFromOptions(PetscDrawLG lg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGDestroy()
```

Example 4 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGSetLegend#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetLegend/

**Contents:**
- PetscDrawLGSetLegend#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

sets the names of each curve plotted

lg - the line graph context.

names - the names for each curve

Call PetscDrawLGGetAxis() and then change properties of the PetscDrawAxis for detailed control of the plot

PetscDrawLGGetAxis(), PetscDrawAxis, PetscDrawAxisSetColors(), PetscDrawAxisSetLabels(), PetscDrawAxisSetHoldLimits()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetLegend(PetscDrawLG lg, const char *const names[])
```

Example 2 (unknown):
```unknown
PetscDrawLGGetAxis()
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawLGGetAxis()
```

---

## PetscDrawLGSetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetLimits/

**Contents:**
- PetscDrawLGSetLimits#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the axis limits for a line graph. If more points are added after this call, the limits will be adjusted to include those additional points.

lg - the line graph context

x_min - the horizontal lower limit

x_max - the horizontal upper limit

y_min - the vertical lower limit

y_max - the vertical upper limit

PetscDrawLGCreate(), PetscDrawLG, PetscDrawAxis

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetLimits(PetscDrawLG lg, PetscReal x_min, PetscReal x_max, PetscReal y_min, PetscReal y_max)
```

Example 2 (unknown):
```unknown
PetscDrawLGCreate()
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscDrawLGSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetOptionsPrefix/

**Contents:**
- PetscDrawLGSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all PetscDrawLG options in the database.

lg - the line graph context

prefix - the prefix to prepend to all option names

PetscDrawLG, PetscDrawLGSetFromOptions(), PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawLG
```

Example 2 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetOptionsPrefix(PetscDrawLG lg, const char prefix[])
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PetscDrawLGSetFromOptions()
```

---

## PetscDrawLGSetUseMarkers#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSetUseMarkers/

**Contents:**
- PetscDrawLGSetUseMarkers#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Causes the line graph object to draw a marker for each data-point.

lg - the linegraph context

flg - should mark each data point

-lg_use_markers (true|false) - true means it draws a marker for each point

PetscDrawLG, PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSetUseMarkers(PetscDrawLG lg, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLGSPDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGSPDraw/

**Contents:**
- PetscDrawLGSPDraw#
- Synopsis#
- Input Parameters#
- Developer Notes#
- See Also#
- Level#
- Location#

Redraws a line graph and a scatter plot on the same PetscDraw they must share

lg - the line graph context

spin - the scatter plot

This code cheats and uses the fact that the PetscDrawLG and PetscDrawSP structs are the same

PetscDrawLGDraw(), PetscDrawSPDraw()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGSPDraw(PetscDrawLG lg, PetscDrawSP spin)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawSP
```

Example 4 (unknown):
```unknown
PetscDrawLGDraw()
```

---

## PetscDrawLGView#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLGView/

**Contents:**
- PetscDrawLGView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

lg - the line graph context

viewer - the viewer to view it with

PetscDrawLG, PetscDrawLGCreate()

src/sys/classes/draw/utils/lgc.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawLGView(PetscDrawLG lg, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscDrawLG
```

Example 3 (unknown):
```unknown
PetscDrawLGCreate()
```

---

## PetscDrawLG#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLG/

**Contents:**
- PetscDrawLG#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

An object that manages drawing simple x-y plots

PetscDrawAxis, PetscDraw, PetscDrawBar, PetscDrawHG, PetscDrawSP, PetscDrawAxisCreate(), PetscDrawLGCreate(), PetscDrawLGAddPoint()

include/petscdrawtypes.h

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

_p_PetscDrawLG in include/petsc/private/drawimpl.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDrawLG *PetscDrawLG;
```

Example 2 (unknown):
```unknown
PetscDrawAxis
```

Example 3 (unknown):
```unknown
PetscDrawBar
```

Example 4 (unknown):
```unknown
PetscDrawHG
```

---

## PetscDrawLineGetWidth#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLineGetWidth/

**Contents:**
- PetscDrawLineGetWidth#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Gets the line width for future draws. The width is relative to the user coordinates of the window; 0.0 denotes the natural width; 1.0 denotes the interior viewport.

draw - the drawing context

width - the width in user coordinates

Not currently implemented.

PetscDraw, PetscDrawLineSetWidth(), PetscDrawLine(), PetscDrawArrow()

src/sys/classes/draw/interface/dline.c

PetscDrawLineGetWidth_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawLineGetWidth_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawLineGetWidth_Win32() in src/sys/classes/draw/impls/win32/win32draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawLineGetWidth(PetscDraw draw, PetscReal *width)
```

Example 2 (unknown):
```unknown
PetscDrawLineSetWidth()
```

Example 3 (unknown):
```unknown
PetscDrawLine()
```

Example 4 (unknown):
```unknown
PetscDrawArrow()
```

---

## PetscDrawLineSetWidth#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLineSetWidth/

**Contents:**
- PetscDrawLineSetWidth#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the line width for future draws. The width is relative to the user coordinates of the window; 0.0 denotes the natural width; 1.0 denotes the entire viewport.

draw - the drawing context

width - the width in user coordinates

PetscDraw, PetscDrawLineGetWidth(), PetscDrawLine(), PetscDrawArrow()

src/sys/classes/draw/interface/dline.c

PetscDrawLineSetWidth_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawLineSetWidth_Win32() in src/sys/classes/draw/impls/win32/win32draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawLineSetWidth(PetscDraw draw, PetscReal width)
```

Example 2 (unknown):
```unknown
PetscDrawLineGetWidth()
```

Example 3 (unknown):
```unknown
PetscDrawLine()
```

Example 4 (unknown):
```unknown
PetscDrawArrow()
```

---

## PetscDrawLine#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawLine/

**Contents:**
- PetscDrawLine#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a line onto a drawable.

draw - the drawing context

xl - horizontal coordinate of first end point

yl - vertical coordinate of first end point

xr - horizontal coordinate of second end point

yr - vertical coordinate of second end point

cl - the colors of the endpoints

PetscDraw, PetscDrawArrow(), PetscDrawLineSetWidth(), PetscDrawLineGetWidth(), PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawPoint()

src/sys/classes/draw/interface/dline.c

PetscDrawLine_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawLine_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawLine_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawLine_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawLine_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawLine(PetscDraw draw, PetscReal xl, PetscReal yl, PetscReal xr, PetscReal yr, int cl)
```

Example 2 (unknown):
```unknown
PetscDrawArrow()
```

Example 3 (unknown):
```unknown
PetscDrawLineSetWidth()
```

Example 4 (unknown):
```unknown
PetscDrawLineGetWidth()
```

---

## PetscDrawMarkerType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawMarkerType/

**Contents:**
- PetscDrawMarkerType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

How a “mark” is indicate in a figure

PETSC_MARKER_CROSS - a small pixel based x symbol or the character x if that is not available

PETSC_MARKER_PLUS - a small pixel based + symbol or the character + if that is not available

PETSC_MARKER_CIRCLE - a small pixel based circle symbol or the character o if that is not available

PETSC_MARKER_POINT - the make obtained with PetscDrawPoint()

PetscDraw, PetscDrawMarker(), PetscDrawSetMarkerType()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_DRAW_MARKER_CROSS,
  PETSC_DRAW_MARKER_POINT,
  PETSC_DRAW_MARKER_PLUS,
  PETSC_DRAW_MARKER_CIRCLE
} PetscDrawMarkerType;
```

Example 2 (unknown):
```unknown
PETSC_MARKER_CROSS
```

Example 3 (unknown):
```unknown
PETSC_MARKER_PLUS
```

Example 4 (unknown):
```unknown
PETSC_MARKER_CIRCLE
```

---

## PetscDrawMarker#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawMarker/

**Contents:**
- PetscDrawMarker#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

draws a marker onto a drawable.

draw - the drawing context

xl - horizontal coordinate of the marker

yl - vertical coordinate of the marker

cl - the color of the marker

PetscDraw, PetscDrawPoint(), PetscDrawString(), PetscDrawSetMarkerType(), PetscDrawGetMarkerType()

src/sys/classes/draw/interface/dmarker.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawMarker(PetscDraw draw, PetscReal xl, PetscReal yl, int cl)
```

Example 2 (unknown):
```unknown
PetscDrawPoint()
```

Example 3 (unknown):
```unknown
PetscDrawString()
```

Example 4 (unknown):
```unknown
PetscDrawSetMarkerType()
```

---

## PetscDrawOpenImage#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawOpenImage/

**Contents:**
- PetscDrawOpenImage#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Opens an image for use with the PetscDraw routines.

comm - the communicator that will share image

filename - optional name of the file where the image will be stored

w - the image width in pixels

h - the image height in pixels

draw - the drawing context.

PetscDraw, PETSC_DRAW_IMAGE, PETSC_DRAW_X, PetscDrawSetSave(), PetscDrawSetFromOptions(), PetscDrawCreate(), PetscDrawDestroy()

src/sys/classes/draw/impls/image/drawimage.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscdraw.h" 
PetscErrorCode PetscDrawOpenImage(MPI_Comm comm, const char filename[], int w, int h, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PETSC_DRAW_IMAGE
```

Example 3 (unknown):
```unknown
PETSC_DRAW_X
```

Example 4 (unknown):
```unknown
PetscDrawSetSave()
```

---

## PetscDrawOpenNull#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawOpenNull/

**Contents:**
- PetscDrawOpenNull#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Opens a null drawing context. All draw commands to it are ignored.

comm - MPI communicator

win - the drawing context

PetscDraw, PetscDrawIsNull(), PETSC_DRAW_NULL, PetscDrawOpenX()

src/sys/classes/draw/impls/null/drawnull.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawOpenNull(MPI_Comm comm, PetscDraw *win)
```

Example 2 (unknown):
```unknown
PetscDrawIsNull()
```

Example 3 (unknown):
```unknown
PETSC_DRAW_NULL
```

Example 4 (unknown):
```unknown
PetscDrawOpenX()
```

---

## PetscDrawOpenX#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawOpenX/

**Contents:**
- PetscDrawOpenX#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Opens an X-window for use with the PetscDraw routines.

comm - the communicator that will share X-window

display - the X display on which to open, or NULL for the local machine

title - the title to put in the title bar, or NULL for no title

x - the x screen coordinates of the upper left corner of window (or PETSC_DECIDE)

y - the y screen coordinates of the upper left corner of window (or PETSC_DECIDE)

w - the screen width in pixels of (or PETSC_DRAW_HALF_SIZE, PETSC_DRAW_FULL_SIZE, or PETSC_DRAW_THIRD_SIZE or PETSC_DRAW_QUARTER_SIZE)

h - the screen height in pixels of (or PETSC_DRAW_HALF_SIZE, PETSC_DRAW_FULL_SIZE, or PETSC_DRAW_THIRD_SIZE or PETSC_DRAW_QUARTER_SIZE)

draw - the drawing context.

-nox - Disables all x-windows output

-display name - Sets name of machine for the X display

-draw_pause pause - Sets time (in seconds) that the program pauses after PetscDrawPause() has been called (0 is default, -1 implies until user input).

-draw_cmap name - Sets the colormap to use.

-draw_cmap_reverse - Reverses the colormap.

-draw_cmap_brighten - Brighten (0 < beta < 1) or darken (-1 < beta < 0) the colormap.

-draw_x_shared_colormap - Causes PETSc to use a shared colormap. By default PETSc creates a separate color for its windows, you must put the mouse into the graphics window to see the correct colors. This options forces PETSc to use the default colormap which will usually result in bad contour plots.

-draw_fast - Does not create colormap for contour plots.

-draw_double_buffer - Uses double buffering for smooth animation.

-geometry - Indicates location and size of window.

If x and y are both PETSC_DECIDE then PETSc places the window automatically.

When finished with the drawing context, it should be destroyed with PetscDrawDestroy().

Whenever indicating null character data in a Fortran code, PETSC_NULL_CHARACTER must be employed. Thus, PETSC_NULL_CHARACTER can be used for the display and title input parameters.

PetscDrawFlush(), PetscDrawDestroy(), PetscDrawCreate()

src/sys/classes/draw/impls/x/drawopenx.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawOpenX(MPI_Comm comm, const char display[], const char title[], int x, int y, int w, int h, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DRAW_HALF_SIZE
```

---

## PetscDrawPause#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPause/

**Contents:**
- PetscDrawPause#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Waits n seconds or until user input, depending on input to PetscDrawSetPause().

draw - the drawing context

PetscDraw, PetscDrawSetPause(), PetscDrawGetPause()

src/sys/classes/draw/interface/dpause.c

PetscDrawPause_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawPause_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawPause_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawSetPause()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPause(PetscDraw draw)
```

Example 3 (unknown):
```unknown
PetscDrawSetPause()
```

Example 4 (unknown):
```unknown
PetscDrawGetPause()
```

---

## PetscDrawPixelToCoordinate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPixelToCoordinate/

**Contents:**
- PetscDrawPixelToCoordinate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

given a pixel in a PetscDraw returns the coordinate

draw - the draw where the coordinates are defined

i - the horizontal pixel location

j - the vertical pixel location

x - the horizontal coordinate

y - the vertical coordinate

src/sys/classes/draw/interface/drect.c

PetscDrawPixelToCoordinate_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawPixelToCoordinate_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawPixelToCoordinate_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPixelToCoordinate(PetscDraw draw, int i, int j, PetscReal *x, PetscReal *y)
```

---

## PetscDrawPointPixel#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPointPixel/

**Contents:**
- PetscDrawPointPixel#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a point onto a drawable, in pixel coordinates

draw - the drawing context

x - horizontal pixel coordinates of the point

y - vertical pixel coordinates of the point

c - the color of the point

PetscDraw, PetscDrawPoint(), PetscDrawPointSetSize()

src/sys/classes/draw/interface/dpoint.c

PetscDrawPointPixel_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawPointPixel_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawPointPixel_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPointPixel(PetscDraw draw, int x, int y, int c)
```

Example 2 (unknown):
```unknown
PetscDrawPoint()
```

Example 3 (unknown):
```unknown
PetscDrawPointSetSize()
```

---

## PetscDrawPointSetSize#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPointSetSize/

**Contents:**
- PetscDrawPointSetSize#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the point size for future draws. The size is relative to the user coordinates of the window; 0.0 denotes the natural width, 1.0 denotes the entire viewport.

draw - the drawing context

width - the width in user coordinates

Even a size of zero insures that a single pixel is colored.

PetscDraw, PetscDrawPoint(), PetscDrawMarker()

src/sys/classes/draw/interface/dpoint.c

PetscDrawPointSetSize_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawPointSetSize_Win32() in src/sys/classes/draw/impls/win32/win32draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPointSetSize(PetscDraw draw, PetscReal width)
```

Example 2 (unknown):
```unknown
PetscDrawPoint()
```

Example 3 (unknown):
```unknown
PetscDrawMarker()
```

---

## PetscDrawPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPoint/

**Contents:**
- PetscDrawPoint#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a point onto a drawable.

draw - the drawing context

xl - horizatonal coordinate of the point

yl - vertical coordinate of the point

cl - the color of the point

PetscDraw, PetscDrawPointPixel(), PetscDrawPointSetSize(), PetscDrawLine(), PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawString(), PetscDrawArrow()

src/sys/classes/draw/interface/dpoint.c

PetscDrawPoint_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawPoint_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawPoint_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawPoint_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPoint(PetscDraw draw, PetscReal xl, PetscReal yl, int cl)
```

Example 2 (unknown):
```unknown
PetscDrawPointPixel()
```

Example 3 (unknown):
```unknown
PetscDrawPointSetSize()
```

Example 4 (unknown):
```unknown
PetscDrawLine()
```

---

## PetscDrawPopCurrentPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPopCurrentPoint/

**Contents:**
- PetscDrawPopCurrentPoint#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Pops a current draw point (discarding it)

draw - the drawing context

PetscDraw, PetscDrawPushCurrentPoint(), PetscDrawSetCurrentPoint(), PetscDrawGetCurrentPoint()

src/sys/classes/draw/interface/dline.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPopCurrentPoint(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawPushCurrentPoint()
```

Example 3 (unknown):
```unknown
PetscDrawSetCurrentPoint()
```

Example 4 (unknown):
```unknown
PetscDrawGetCurrentPoint()
```

---

## PetscDrawPushCurrentPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawPushCurrentPoint/

**Contents:**
- PetscDrawPushCurrentPoint#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Pushes a new current draw point, retaining the old one, some codes use this point to determine where to draw next

draw - the drawing context

x - horizontal coordinate of the current point

y - vertical coordinate of the current point

PetscDraw, PetscDrawPopCurrentPoint(), PetscDrawGetCurrentPoint()

src/sys/classes/draw/interface/dline.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawPushCurrentPoint(PetscDraw draw, PetscReal x, PetscReal y)
```

Example 2 (unknown):
```unknown
PetscDrawPopCurrentPoint()
```

Example 3 (unknown):
```unknown
PetscDrawGetCurrentPoint()
```

---

## PetscDrawRealToColor#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawRealToColor/

**Contents:**
- PetscDrawRealToColor#
- Synopsis#
- Input Parameters#
- Returns#
- Note#
- See Also#
- Level#
- Location#

Maps a real value within an interval to a color. The color is an integer value in the range [PETSC_DRAW_BASIC_COLORS to 255] that can be passed to various drawing routines.

value - value to map within the interval [min, max]

min - lower end of interval

max - upper end of interval

The result as integer

Values outside the interval [min, max] are clipped.

PetscDraw, PetscDrawPointPixel(), PetscDrawPoint(), PetscDrawLine(), PetscDrawTriangle(), PetscDrawRectangle()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_DRAW_BASIC_COLORS
```

Example 2 (cpp):
```cpp
#include <petscdraw.h>
int PetscDrawRealToColor(PetscReal value,PetscReal min,PetscReal max)
```

Example 3 (unknown):
```unknown
PetscDrawPointPixel()
```

Example 4 (unknown):
```unknown
PetscDrawPoint()
```

---

## PetscDrawRectangle#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawRectangle/

**Contents:**
- PetscDrawRectangle#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a rectangle onto a PetscDraw object

draw - the drawing context

xl - coordinates of the lower left corner

yl - coordinates of the lower left corner

xr - coordinate of the upper right corner

yr - coordinate of the upper right corner

c1 - the color of the first corner

c2 - the color of the second corner

c3 - the color of the third corner

c4 - the color of the fourth corner

PetscDraw, PetscDrawLine(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawPoint(), PetscDrawString(), PetscDrawArrow()

src/sys/classes/draw/interface/drect.c

PetscDrawRectangle_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawRectangle_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawRectangle_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawRectangle_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawRectangle_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawRectangle(PetscDraw draw, PetscReal xl, PetscReal yl, PetscReal xr, PetscReal yr, int c1, int c2, int c3, int c4)
```

Example 2 (unknown):
```unknown
PetscDrawLine()
```

Example 3 (unknown):
```unknown
PetscDrawTriangle()
```

Example 4 (unknown):
```unknown
PetscDrawEllipse()
```

---

## PetscDrawRegisterAll#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawRegisterAll/

**Contents:**
- PetscDrawRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the graphics methods in the PetscDraw package.

PetscDraw, PetscDrawType, PetscDrawRegisterDestroy()

src/sys/classes/draw/interface/drawregall.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscDrawType
```

Example 3 (unknown):
```unknown
PetscDrawRegisterDestroy()
```

---

## PetscDrawRegister#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawRegister/

**Contents:**
- PetscDrawRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a method to the graphics package.

Not Collective, No Fortran Support

sname - name of a new user-defined graphics class

function - routine to create method context

PetscDrawRegister() may be called multiple times to add several user-defined graphics classes

Then, your specific graphics package can be chosen with the procedural interface via

or at runtime via the option

PetscDraw, PetscDrawRegisterAll(), PetscDrawRegisterDestroy(), PetscDrawType, PetscDrawSetType()

src/sys/classes/draw/interface/drawreg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawRegister(const char *sname, PetscErrorCode (*function)(PetscDraw))
```

Example 2 (unknown):
```unknown
PetscDrawRegister()
```

Example 3 (unknown):
```unknown
PetscDrawRegister("my_draw_type", MyDrawCreate);
```

Example 4 (unknown):
```unknown
PetscDrawSetType(ksp, "my_draw_type")
```

---

## PetscDrawResizeWindow#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawResizeWindow/

**Contents:**
- PetscDrawResizeWindow#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Allows one to resize a window from a program.

w - the new width of the window

h - the new height of the window

PetscDraw, PetscDrawCheckResizedWindow()

src/sys/classes/draw/interface/draw.c

PetscDrawResizeWindow_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawResizeWindow_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawResizeWindow_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawResizeWindow(PetscDraw draw, int w, int h)
```

Example 2 (unknown):
```unknown
PetscDrawCheckResizedWindow()
```

---

## PetscDrawRestoreSingleton#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawRestoreSingleton/

**Contents:**
- PetscDrawRestoreSingleton#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Remove access to a PetscDraw object obtained with PetscDrawGetSingleton() by the one process.

draw - the original window

sdraw - the singleton window

PetscDraw, PetscDrawGetSingleton(), PetscViewerGetSingleton(), PetscViewerRestoreSingleton()

src/sys/classes/draw/interface/draw.c

PetscDrawRestoreSingleton_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawRestoreSingleton_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawRestoreSingleton_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawGetSingleton()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawRestoreSingleton(PetscDraw draw, PetscDraw *sdraw)
```

Example 3 (unknown):
```unknown
PetscDrawGetSingleton()
```

Example 4 (unknown):
```unknown
PetscViewerGetSingleton()
```

---

## PetscDrawSaveMovie#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSaveMovie/

**Contents:**
- PetscDrawSaveMovie#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Saves a movie from previously saved images

draw - the drawing context

This is not normally called by the user.

The ffmpeg utility must be in your path to make the movie.

PetscDraw, PetscDrawSetSave(), PetscDrawSetSaveMovie()

src/sys/classes/draw/interface/dsave.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSaveMovie(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawSetSave()
```

Example 3 (unknown):
```unknown
PetscDrawSetSaveMovie()
```

---

## PetscDrawSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSave/

**Contents:**
- PetscDrawSave#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

draw - the drawing context

this is not normally called by the user.

PetscDraw, PetscDrawSetSave()

src/sys/classes/draw/interface/dsave.c

PetscDrawSave_Image() in src/sys/classes/draw/impls/image/drawimage.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSave(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawSetSave()
```

---

## PetscDrawScalePopup#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawScalePopup/

**Contents:**
- PetscDrawScalePopup#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

draws a contour scale window.

popup - the window (often a window obtained via PetscDrawGetPopup()

min - minimum value being plotted

max - maximum value being plotted

All processors that share the draw MUST call this routine

PetscDraw, PetscDrawGetPopup(), PetscDrawTensorContour()

src/sys/classes/draw/interface/dtri.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawScalePopup(PetscDraw popup, PetscReal min, PetscReal max)
```

Example 2 (unknown):
```unknown
PetscDrawGetPopup()
```

Example 3 (unknown):
```unknown
PetscDrawGetPopup()
```

Example 4 (unknown):
```unknown
PetscDrawTensorContour()
```

---

## PetscDrawSetCoordinates#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetCoordinates/

**Contents:**
- PetscDrawSetCoordinates#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the application coordinates of the corners of the window (or page).

draw - the drawing object

xl - the lower left x coordinate

yl - the lower left y coordinate

xr - the upper right x coordinate

yr - the upper right y coordinate

PetscDraw, PetscDrawGetCoordinates()

src/sys/classes/draw/interface/dcoor.c

PetscDrawSetCoordinates_Image() in src/sys/classes/draw/impls/image/drawimage.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetCoordinates(PetscDraw draw, PetscReal xl, PetscReal yl, PetscReal xr, PetscReal yr)
```

Example 2 (unknown):
```unknown
PetscDrawGetCoordinates()
```

---

## PetscDrawSetCurrentPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetCurrentPoint/

**Contents:**
- PetscDrawSetCurrentPoint#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the current draw point, some codes use this point to determine where to draw next

draw - the drawing context

x - horizontal coordinate of the current point

y - vertical coordinate of the current point

PetscDraw, PetscDrawPushCurrentPoint(), PetscDrawPopCurrentPoint(), PetscDrawGetCurrentPoint()

src/sys/classes/draw/interface/dline.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetCurrentPoint(PetscDraw draw, PetscReal x, PetscReal y)
```

Example 2 (unknown):
```unknown
PetscDrawPushCurrentPoint()
```

Example 3 (unknown):
```unknown
PetscDrawPopCurrentPoint()
```

Example 4 (unknown):
```unknown
PetscDrawGetCurrentPoint()
```

---

## PetscDrawSetDisplay#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetDisplay/

**Contents:**
- PetscDrawSetDisplay#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the display where a PetscDraw object will be displayed

draw - the drawing context

display - the X windows display

PetscDraw, PetscDrawOpenX(), PetscDrawCreate()

src/sys/classes/draw/interface/draw.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetDisplay(PetscDraw draw, const char display[])
```

Example 2 (unknown):
```unknown
PetscDrawOpenX()
```

Example 3 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawSetDoubleBuffer#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetDoubleBuffer/

**Contents:**
- PetscDrawSetDoubleBuffer#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets a window to be double buffered.

draw - the drawing context

PetscDraw, PetscDrawOpenX(), PetscDrawCreate()

src/sys/classes/draw/interface/draw.c

src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ts/tutorials/ex21.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c src/ts/tutorials/ex2.c

PetscDrawSetDoubleBuffer_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawSetDoubleBuffer_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawSetDoubleBuffer_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetDoubleBuffer(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawOpenX()
```

Example 3 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetFromOptions/

**Contents:**
- PetscDrawSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the graphics type from the options database. Defaults to a PETSc X Windows graphics.

draw - the graphics context

-nox - do not use X graphics (ignore graphics calls, but run program correctly)

-nox_warning - when X Windows support is not installed this prevents the warning message from being printed

-draw_pause seconds - -1 indicates wait for mouse input, -2 indicates pause when window is to be destroyed

-draw_marker_type (x|point) - set the marker type

-draw_save [filename] - (X Windows only) saves each image before it is cleared to a file

-draw_save_final_image [filename] - (X Windows only) saves the final image displayed in a window

-draw_save_movie - converts image files to a movie at the end of the run. See PetscDrawSetSave()

-draw_save_single_file - saves each new image in the same file, normally each new image is saved in a new file with ‘filename/filename_%d.ext’

-draw_save_on_clear - saves an image on each clear, mainly for debugging

-draw_save_on_flush - saves an image on each flush, mainly for debugging

Must be called after PetscDrawCreate() before the PetscDraw is used.

PetscDraw, PetscDrawCreate(), PetscDrawSetType(), PetscDrawSetSave(), PetscDrawSetSaveFinalImage(), PetscDrawPause(), PetscDrawSetPause()

src/sys/classes/draw/interface/drawreg.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawSetFromOptions(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawSetSave()
```

Example 3 (unknown):
```unknown
PetscDrawCreate()
```

Example 4 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawSetMarkerType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetMarkerType/

**Contents:**
- PetscDrawSetMarkerType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

sets the type of marker to display with PetscDrawMarker()

draw - the drawing context

mtype - either PETSC_DRAW_MARKER_CROSS (default) or PETSC_DRAW_MARKER_POINT

-draw_marker_type - x or point

PetscDraw, PetscDrawPoint(), PetscDrawMarker(), PetscDrawGetMarkerType(), PetscDrawMarkerType

src/sys/classes/draw/interface/dmarker.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawMarker()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetMarkerType(PetscDraw draw, PetscDrawMarkerType mtype)
```

Example 3 (unknown):
```unknown
PETSC_DRAW_MARKER_CROSS
```

Example 4 (unknown):
```unknown
PETSC_DRAW_MARKER_POINT
```

---

## PetscDrawSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetOptionsPrefix/

**Contents:**
- PetscDrawSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all PetscDraw options in the database.

draw - the draw context

prefix - the prefix to prepend to all option names

PetscDraw, PetscDrawSetFromOptions(), PetscDrawCreate()

src/sys/classes/draw/interface/drawreg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawSetOptionsPrefix(PetscDraw draw, const char prefix[])
```

Example 2 (unknown):
```unknown
PetscDrawSetFromOptions()
```

Example 3 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDrawSetPause#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetPause/

**Contents:**
- PetscDrawSetPause#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the amount of time that program pauses after a PetscDrawPause() is called.

draw - the drawing object

lpause - number of seconds to pause, -1 implies until user input, -2 pauses only on the PetscDrawDestroy()

-draw_pause value - set the time to pause

By default the pause time is zero unless the -draw_pause option is given during PetscDrawCreate().

PetscDraw, PetscDrawGetPause(), PetscDrawPause()

src/sys/classes/draw/interface/dpause.c

src/ksp/ksp/tutorials/ex68.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawPause()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetPause(PetscDraw draw, PetscReal lpause)
```

Example 3 (unknown):
```unknown
PetscDrawDestroy()
```

Example 4 (unknown):
```unknown
PetscDrawGetPause()
```

---

## PetscDrawSetSaveFinalImage#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetSaveFinalImage/

**Contents:**
- PetscDrawSetSaveFinalImage#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Saves the final image produced in a PetscDraw into a file

draw - the graphics context

filename - name of the file, if NULL or empty uses name set with PetscDrawSetSave() or the name of the draw object

-draw_save_final_image filename - filename could be name.ext or .ext (where .ext determines the type of graphics file to save, for example .png)

You should call this BEFORE creating your image and calling PetscDrawSave().

The supported image types are .png, .gif, and .ppm (PETSc chooses the default in that order).

PetscDraw, PetscDrawSetSave(), PetscDrawSetFromOptions(), PetscDrawCreate(), PetscDrawDestroy()

src/sys/classes/draw/interface/dsave.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetSaveFinalImage(PetscDraw draw, const char filename[])
```

Example 2 (unknown):
```unknown
PetscDrawSetSave()
```

Example 3 (unknown):
```unknown
PetscDrawSave()
```

Example 4 (unknown):
```unknown
Support for .png images requires configure --with-libpng.
   Support for .gif images requires configure --with-giflib.
   Support for .jpg images requires configure --with-libjpeg.
   Support for .ppm images is built-in. The PPM format has no compression (640x480 pixels ~ 900 KiB).
```

---

## PetscDrawSetSaveMovie#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetSaveMovie/

**Contents:**
- PetscDrawSetSaveMovie#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Saves a movie produced from a PetscDraw into a file

draw - the graphics context

movieext - optional extension defining the movie format

-draw_save_movie .ext - saves a movie with extension .ext

You should call this AFTER calling PetscDrawSetSave() and BEFORE creating your image with PetscDrawSave(). The ffmpeg utility must be in your path to make the movie.

PetscDraw, PetscDrawSetSave(), PetscDrawSetFromOptions(), PetscDrawCreate(), PetscDrawDestroy()

src/sys/classes/draw/interface/dsave.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetSaveMovie(PetscDraw draw, const char movieext[])
```

Example 2 (unknown):
```unknown
PetscDrawSetSave()
```

Example 3 (unknown):
```unknown
PetscDrawSave()
```

Example 4 (unknown):
```unknown
PetscDrawSetSave()
```

---

## PetscDrawSetSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetSave/

**Contents:**
- PetscDrawSetSave#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Saves images produced in a PetscDraw into a file

draw - the graphics context

filename - name of the file, if .ext then uses name of draw object plus .ext using .ext to determine the image type

-draw_save filename filename - filename could be name.ext or .ext (where .ext determines the type of graphics file to save, for example .png)

-draw_save_final_image [filename] - saves the final image displayed in a window

-draw_save_single_file - saves each new image in the same file, normally each new image is saved in a new file with filename/filename_%d.ext

You should call this BEFORE creating your image and calling PetscDrawSave(). The supported image types are .png, .gif, .jpg, and .ppm (PETSc chooses the default in that order). Support for .png images requires configure –with-libpng. Support for .gif images requires configure –with-giflib. Support for .jpg images requires configure –with-libjpeg. Support for .ppm images is built-in. The PPM format has no compression (640x480 pixels ~ 900 KiB).

PetscDraw, PetscDrawOpenX(), PetscDrawOpenImage(), PetscDrawSetFromOptions(), PetscDrawCreate(), PetscDrawDestroy(), PetscDrawSetSaveFinalImage()

src/sys/classes/draw/interface/dsave.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetSave(PetscDraw draw, const char filename[])
```

Example 2 (unknown):
```unknown
PetscDrawSave()
```

Example 3 (unknown):
```unknown
PetscDrawOpenX()
```

Example 4 (unknown):
```unknown
PetscDrawOpenImage()
```

---

## PetscDrawSetTitle#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetTitle/

**Contents:**
- PetscDrawSetTitle#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the title of a PetscDraw context.

draw - the graphics context

The title is positioned in the windowing system title bar for the window. Hence it will not be saved with -draw_save in the image.

A copy of the string is made, so you may destroy the title string after calling this routine.

You can use PetscDrawAxisSetLabels() to indicate a title within the window

PetscDraw, PetscDrawGetTitle(), PetscDrawAppendTitle()

src/sys/classes/draw/interface/draw.c

PetscDrawSetTitle_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawSetTitle_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawSetTitle_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetTitle(PetscDraw draw, const char title[])
```

Example 2 (unknown):
```unknown
PetscDrawAxisSetLabels()
```

Example 3 (unknown):
```unknown
PetscDrawGetTitle()
```

Example 4 (unknown):
```unknown
PetscDrawAppendTitle()
```

---

## PetscDrawSetType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetType/

**Contents:**
- PetscDrawSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Builds graphics object for a particular implementation

draw - the graphics context

type - for example, PETSC_DRAW_X

-draw_type (x|null|win32|tikz|image) - Sets the type; see PetscDrawType

See PetscDrawSetFromOptions() for additional options database keys

See PetscDrawType for available methods (for instance, PETSC_DRAW_X, PETSC_DRAW_TIKZ or PETSC_DRAW_IMAGE)

PetscDraw, PETSC_DRAW_X, PETSC_DRAW_TIKZ, PETSC_DRAW_IMAGE, PetscDrawSetFromOptions(), PetscDrawCreate(), PetscDrawDestroy(), PetscDrawType

src/sys/classes/draw/interface/drawreg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawSetType(PetscDraw draw, PetscDrawType type)
```

Example 2 (unknown):
```unknown
PETSC_DRAW_X
```

Example 3 (unknown):
```unknown
PetscDrawType
```

Example 4 (unknown):
```unknown
PetscDrawSetFromOptions()
```

---

## PetscDrawSetViewPort#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetViewPort/

**Contents:**
- PetscDrawSetViewPort#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the portion of the window (page) to which draw routines will write.

xl - the horizontal coordinate of the lower left corner of the subwindow.

yl - the vertical coordinate of the lower left corner of the subwindow.

xr - the horizontal coordinate of the upper right corner of the subwindow.

yr - the vertical coordinate of the upper right corner of the subwindow.

draw - the drawing context

These numbers must always be between 0.0 and 1.0.

Lower left corner is (0,0).

PetscDrawGetViewPort(), PetscDraw, PetscDrawSplitViewPort(), PetscDrawViewPortsCreate()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetViewPort(PetscDraw draw, PetscReal xl, PetscReal yl, PetscReal xr, PetscReal yr)
```

Example 2 (unknown):
```unknown
PetscDrawGetViewPort()
```

Example 3 (unknown):
```unknown
PetscDrawSplitViewPort()
```

Example 4 (unknown):
```unknown
PetscDrawViewPortsCreate()
```

---

## PetscDrawSetVisible#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSetVisible/

**Contents:**
- PetscDrawSetVisible#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets if the drawing surface (the ‘window’) is visible on its display.

draw - the drawing window

visible - if the surface should be visible

src/sys/classes/draw/interface/draw.c

PetscDrawSetVisible_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawSetVisible_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSetVisible(PetscDraw draw, PetscBool visible)
```

---

## PetscDrawSPAddPointColorized#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPointColorized/

**Contents:**
- PetscDrawSPAddPointColorized#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds another point to each of the scatter plots as well as a numeric value to be used to colorize the scatter point.

sp - the scatter plot data structure

x - array of length dim containing the new x coordinate values for each of the point curves.

y - array of length dim containing the new y coordinate values for each of the point curves.

z - array of length dim containing the numeric values that will be mapped to [0,255] and used for scatter point colors.

The dimensions of the arrays is the number of point curves passed to PetscDrawSPCreate(). The new points will not be displayed until a call to PetscDrawSPDraw() is made

PetscDrawSPAddPoints(), PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPReset(), PetscDrawSPDraw(), PetscDrawSPAddPoint()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPAddPointColorized(PetscDrawSP sp, PetscReal *x, PetscReal *y, PetscReal *z)
```

Example 2 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 3 (unknown):
```unknown
PetscDrawSPDraw()
```

Example 4 (unknown):
```unknown
PetscDrawSPAddPoints()
```

---

## PetscDrawSPAddPoints#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPoints/

**Contents:**
- PetscDrawSPAddPoints#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds several points to each of the scatter plot point curves.

sp - the scatter plot context

xx - array of pointers that point to arrays containing the new x coordinates for each curve.

yy - array of pointers that point to arrays containing the new y points for each curve.

n - number of points being added, each represents a subarray of length dim where dim is the value from PetscDrawSPGetDimension()

The new points will not be displayed until a call to PetscDrawSPDraw() is made

PetscDrawSPAddPoint(), PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPReset(), PetscDrawSPDraw(), PetscDrawSPAddPointColorized()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPAddPoints(PetscDrawSP sp, int n, PetscReal *xx[], PetscReal *yy[])
```

Example 2 (unknown):
```unknown
PetscDrawSPGetDimension()
```

Example 3 (unknown):
```unknown
PetscDrawSPDraw()
```

Example 4 (unknown):
```unknown
PetscDrawSPAddPoint()
```

---

## PetscDrawSPAddPoint#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPAddPoint/

**Contents:**
- PetscDrawSPAddPoint#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds another point to each of the scatter plot point curves.

sp - the scatter plot data structure

x - the x coordinate values (of length dim) for the points of the curve

y - the y coordinate values (of length dim) for the points of the curve

Here dim is the number of point curves passed to PetscDrawSPCreate(). The new points will not be displayed until a call to PetscDrawSPDraw() is made.

PetscDrawSPAddPoints(), PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPReset(), PetscDrawSPDraw(), PetscDrawSPAddPointColorized()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPAddPoint(PetscDrawSP sp, PetscReal *x, PetscReal *y)
```

Example 2 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 3 (unknown):
```unknown
PetscDrawSPDraw()
```

Example 4 (unknown):
```unknown
PetscDrawSPAddPoints()
```

---

## PetscDrawSPCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPCreate/

**Contents:**
- PetscDrawSPCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a scatter plot data structure.

draw - the window where the graph will be made.

dim - the number of sets of points which will be drawn

drawsp - the scatter plot context

Add points to the plot with PetscDrawSPAddPoint() or PetscDrawSPAddPoints(); the new points are not displayed until PetscDrawSPDraw() is called.

PetscDrawSPReset() removes all the points that have been added

PetscDrawSPSetDimension() determines how many point curves are being plotted.

The MPI communicator that owns the PetscDraw owns this PetscDrawSP, and each process can add points. All MPI ranks in the communicator must call PetscDrawSPDraw() to display the updated graph.

PetscDrawLGCreate(), PetscDrawLG, PetscDrawBarCreate(), PetscDrawBar, PetscDrawHGCreate(), PetscDrawHG, PetscDrawSPDestroy(), PetscDraw, PetscDrawSP, PetscDrawSPSetDimension(), PetscDrawSPReset(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints(), PetscDrawSPDraw(), PetscDrawSPSave(), PetscDrawSPSetLimits(), PetscDrawSPGetAxis(), PetscDrawAxis, PetscDrawSPGetDraw()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPCreate(PetscDraw draw, int dim, PetscDrawSP *drawsp)
```

Example 2 (unknown):
```unknown
PetscDrawSPAddPoint()
```

Example 3 (unknown):
```unknown
PetscDrawSPAddPoints()
```

Example 4 (unknown):
```unknown
PetscDrawSPDraw()
```

---

## PetscDrawSPDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPDestroy/

**Contents:**
- PetscDrawSPDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees all space taken up by scatter plot data structure.

sp - the scatter plot context

PetscDrawSPCreate(), PetscDrawSP, PetscDrawSPReset()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPDestroy(PetscDrawSP *sp)
```

Example 2 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 3 (unknown):
```unknown
PetscDrawSP
```

Example 4 (unknown):
```unknown
PetscDrawSPReset()
```

---

## PetscDrawSPDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPDraw/

**Contents:**
- PetscDrawSPDraw#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Redraws a scatter plot.

sp - the scatter plot context

clear - clear the window before drawing the new plot

PetscDrawLGDraw(), PetscDrawLGSPDraw(), PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPReset(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPDraw(PetscDrawSP sp, PetscBool clear)
```

Example 2 (unknown):
```unknown
PetscDrawLGDraw()
```

Example 3 (unknown):
```unknown
PetscDrawLGSPDraw()
```

Example 4 (unknown):
```unknown
PetscDrawSP
```

---

## PetscDrawSPGetAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPGetAxis/

**Contents:**
- PetscDrawSPGetAxis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the axis context associated with a scatter plot

sp - the scatter plot context

axis - the axis context

This is useful if one wants to change some axis property, such as labels, color, etc. The axis context should not be destroyed by the application code.

PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPDraw(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints(), PetscDrawAxis, PetscDrawAxisCreate()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPGetAxis(PetscDrawSP sp, PetscDrawAxis *axis)
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 4 (unknown):
```unknown
PetscDrawSPDraw()
```

---

## PetscDrawSPGetDimension#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPGetDimension/

**Contents:**
- PetscDrawSPGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of sets of points that are to be drawn at each PetscDrawSPAddPoint()

sp - the scatter plot context.

dim - the number of point curves on this process

PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawSPAddPoint()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPGetDimension(PetscDrawSP sp, int *dim)
```

Example 3 (unknown):
```unknown
PetscDrawSP
```

Example 4 (unknown):
```unknown
PetscDrawSPCreate()
```

---

## PetscDrawSPGetDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPGetDraw/

**Contents:**
- PetscDrawSPGetDraw#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the draw context associated with a scatter plot

sp - the scatter plot context

draw - the draw context

PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPDraw(), PetscDraw

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPGetDraw(PetscDrawSP sp, PetscDraw *draw)
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 4 (unknown):
```unknown
PetscDrawSPDraw()
```

---

## PetscDrawSplitViewPort#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSplitViewPort/

**Contents:**
- PetscDrawSplitViewPort#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Splits a window shared by several processes into smaller view ports. One for each process.

draw - the drawing context

PetscDrawDivideViewPort(), PetscDrawSetViewPort()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawSplitViewPort(PetscDraw draw)
```

Example 2 (unknown):
```unknown
PetscDrawDivideViewPort()
```

Example 3 (unknown):
```unknown
PetscDrawSetViewPort()
```

---

## PetscDrawSPReset#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPReset/

**Contents:**
- PetscDrawSPReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears scatter plot to allow for reuse with new data.

sp - the scatter plot context.

PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints(), PetscDrawSPDraw()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPReset(PetscDrawSP sp)
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 4 (unknown):
```unknown
PetscDrawSPAddPoint()
```

---

## PetscDrawSPSave#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPSave/

**Contents:**
- PetscDrawSPSave#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

sp - the scatter plot context

PetscDrawSPCreate(), PetscDrawSPGetDraw(), PetscDrawSetSave(), PetscDrawSave()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPSave(PetscDrawSP sp)
```

Example 2 (unknown):
```unknown
PetscDrawSPCreate()
```

Example 3 (unknown):
```unknown
PetscDrawSPGetDraw()
```

Example 4 (unknown):
```unknown
PetscDrawSetSave()
```

---

## PetscDrawSPSetDimension#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPSetDimension/

**Contents:**
- PetscDrawSPSetDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Change the number of points that are added at each PetscDrawSPAddPoint()

sp - the scatter plot context.

dim - the number of point curves on this process

PetscDrawSP, PetscDrawSPCreate(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawSPAddPoint()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPSetDimension(PetscDrawSP sp, int dim)
```

Example 3 (unknown):
```unknown
PetscDrawSP
```

Example 4 (unknown):
```unknown
PetscDrawSPCreate()
```

---

## PetscDrawSPSetLimits#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSPSetLimits/

**Contents:**
- PetscDrawSPSetLimits#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the axis limits for a scatter plot. If more points are added after this call, the limits will be adjusted to include those additional points.

sp - the line graph context

x_min - the horizontal lower limit

x_max - the horizontal upper limit

y_min - the vertical lower limit

y_max - the vertical upper limit

PetscDrawSP, PetscDrawAxis, PetscDrawSPCreate(), PetscDrawSPDraw(), PetscDrawSPAddPoint(), PetscDrawSPAddPoints(), PetscDrawSPGetAxis()

src/sys/classes/draw/utils/dscatter.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscsys.h" 
PetscErrorCode PetscDrawSPSetLimits(PetscDrawSP sp, PetscReal x_min, PetscReal x_max, PetscReal y_min, PetscReal y_max)
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (unknown):
```unknown
PetscDrawAxis
```

Example 4 (unknown):
```unknown
PetscDrawSPCreate()
```

---

## PetscDrawSP#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawSP/

**Contents:**
- PetscDrawSP#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

An object that manages drawing scatter plots

PetscDrawAxis, PetscDraw, PetscDrawLG, PetscDrawBar, PetscDrawHG, PetscDrawSPCreate()

include/petscdrawtypes.h

_p_PetscDrawSP in include/petsc/private/drawimpl.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDrawSP *PetscDrawSP;
```

Example 2 (unknown):
```unknown
PetscDrawAxis
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PetscDrawBar
```

---

## PetscDrawStringBoxed#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawStringBoxed/

**Contents:**
- PetscDrawStringBoxed#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Draws a string with a box around it

draw - the drawing context

sxl - the coordinates of center of the box

syl - the coordinates of top line of box

sc - the color of the text

bc - the color of the bounding box

text - the text to draw

w - the width of the resulting box (optional)

h - the height of resulting box (optional)

PetscDraw, PetscDrawStringVertical(), PetscDrawString(), PetscDrawStringCentered(), PetscDrawStringSetSize(), PetscDrawStringGetSize()

src/sys/classes/draw/interface/dtext.c

PetscDrawStringBoxed_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawStringBoxed_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawStringBoxed_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawStringBoxed(PetscDraw draw, PetscReal sxl, PetscReal syl, int sc, int bc, const char text[], PetscReal *w, PetscReal *h)
```

Example 2 (unknown):
```unknown
PetscDrawStringVertical()
```

Example 3 (unknown):
```unknown
PetscDrawString()
```

Example 4 (unknown):
```unknown
PetscDrawStringCentered()
```

---

## PetscDrawStringCentered#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawStringCentered/

**Contents:**
- PetscDrawStringCentered#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

draws text onto a drawable centered at a point

draw - the drawing context

xc - the coordinates of right-left center of text

yl - the coordinates of lower edge of text

cl - the color of the text

text - the text to draw

PetscDraw, PetscDrawStringVertical(), PetscDrawString(), PetscDrawStringBoxed(), PetscDrawStringSetSize(), PetscDrawStringGetSize()

src/sys/classes/draw/interface/dtext.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawStringCentered(PetscDraw draw, PetscReal xc, PetscReal yl, int cl, const char text[])
```

Example 2 (unknown):
```unknown
PetscDrawStringVertical()
```

Example 3 (unknown):
```unknown
PetscDrawString()
```

Example 4 (unknown):
```unknown
PetscDrawStringBoxed()
```

---

## PetscDrawStringGetSize#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawStringGetSize/

**Contents:**
- PetscDrawStringGetSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Gets the size for character text. The width is relative to the user coordinates of the window.

draw - the drawing context

width - the width in user coordinates

height - the character height

PetscDraw, PetscDrawStringVertical(), PetscDrawString(), PetscDrawStringCentered(), PetscDrawStringBoxed(), PetscDrawStringSetSize()

src/sys/classes/draw/interface/dtext.c

PetscDrawStringGetSize_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawStringGetSize_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawStringGetSize_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawStringGetSize_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawStringGetSize_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawStringGetSize(PetscDraw draw, PetscReal *width, PetscReal *height)
```

Example 2 (unknown):
```unknown
PetscDrawStringVertical()
```

Example 3 (unknown):
```unknown
PetscDrawString()
```

Example 4 (unknown):
```unknown
PetscDrawStringCentered()
```

---

## PetscDrawStringSetSize#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawStringSetSize/

**Contents:**
- PetscDrawStringSetSize#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the size for character text.

draw - the drawing context

width - the width in user coordinates

height - the character height in user coordinates

Only a limited range of sizes are available.

PetscDraw, PetscDrawStringVertical(), PetscDrawString(), PetscDrawStringCentered(), PetscDrawStringBoxed(), PetscDrawStringGetSize()

src/sys/classes/draw/interface/dtext.c

PetscDrawStringSetSize_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawStringSetSize_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawStringSetSize_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawStringSetSize(PetscDraw draw, PetscReal width, PetscReal height)
```

Example 2 (unknown):
```unknown
PetscDrawStringVertical()
```

Example 3 (unknown):
```unknown
PetscDrawString()
```

Example 4 (unknown):
```unknown
PetscDrawStringCentered()
```

---

## PetscDrawStringVertical#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawStringVertical/

**Contents:**
- PetscDrawStringVertical#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws text onto a drawable.

draw - the drawing context

xl - coordinate of upper left corner of text

yl - coordinate of upper left corner of text

cl - the color of the text

text - the text to draw

PetscDraw, PetscDrawString(), PetscDrawStringCentered(), PetscDrawStringBoxed(), PetscDrawStringSetSize(), PetscDrawStringGetSize()

src/sys/classes/draw/interface/dtext.c

PetscDrawStringVertical_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawStringVertical_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawStringVertical_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawStringVertical_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawStringVertical_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawStringVertical(PetscDraw draw, PetscReal xl, PetscReal yl, int cl, const char text[])
```

Example 2 (unknown):
```unknown
PetscDrawString()
```

Example 3 (unknown):
```unknown
PetscDrawStringCentered()
```

Example 4 (unknown):
```unknown
PetscDrawStringBoxed()
```

---

## PetscDrawString#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawString/

**Contents:**
- PetscDrawString#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws text onto a drawable.

draw - the drawing context

xl - coordinate of lower left corner of text

yl - coordinate of lower left corner of text

cl - the color of the text

text - the text to draw

PetscDraw, PetscDrawStringVertical(), PetscDrawStringCentered(), PetscDrawStringBoxed(), PetscDrawStringSetSize(), PetscDrawStringGetSize(), PetscDrawLine(), PetscDrawRectangle(), PetscDrawTriangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawPoint()

src/sys/classes/draw/interface/dtext.c

PetscDrawString_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawString_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawString_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawString_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawString_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawString(PetscDraw draw, PetscReal xl, PetscReal yl, int cl, const char text[])
```

Example 2 (unknown):
```unknown
PetscDrawStringVertical()
```

Example 3 (unknown):
```unknown
PetscDrawStringCentered()
```

Example 4 (unknown):
```unknown
PetscDrawStringBoxed()
```

---

## PetscDrawTensorContourPatch#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawTensorContourPatch/

**Contents:**
- PetscDrawTensorContourPatch#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

draws a rectangular patch of a contour plot for a two-dimensional array.

draw - the draw context

m - the number of local mesh points in the x direction

n - the number of local mesh points in the y direction

x - the horizontal locations of the local mesh points

y - the vertical locations of the local mesh points

min - the minimum value in the entire contour

max - the maximum value in the entire contour

-draw_x_shared_colormap - Activates private colormap

This is a lower level support routine, usually the user will call PetscDrawTensorContour().

PetscDraw, PetscDrawTensorContour()

src/sys/classes/draw/interface/dtri.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawTensorContourPatch(PetscDraw draw, int m, int n, PetscReal *x, PetscReal *y, PetscReal min, PetscReal max, PetscReal *v)
```

Example 2 (unknown):
```unknown
PetscDrawTensorContour()
```

Example 3 (unknown):
```unknown
PetscDrawTensorContour()
```

---

## PetscDrawTensorContour#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawTensorContour/

**Contents:**
- PetscDrawTensorContour#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#

draws a contour plot for a two-dimensional array

Collective, but draw must be sequential

draw - the draw context

m - the number of local mesh points in the x direction

n - the number of local mesh points in the y direction

xi - the locations of the global mesh points in the horizontal direction (optional, use NULL to indicate uniform spacing on [0,1])

yi - the locations of the global mesh points in the vertical direction (optional, use NULL to indicate uniform spacing on [0,1])

-draw_x_shared_colormap - Indicates use of private colormap

-draw_contour_grid - draws grid contour

PetscDraw, PetscDrawTensorContourPatch(), PetscDrawScalePopup()

src/sys/classes/draw/interface/dtri.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawTensorContour(PetscDraw draw, int m, int n, const PetscReal xi[], const PetscReal yi[], PetscReal v[])
```

Example 2 (unknown):
```unknown
PetscDrawTensorContourPatch()
```

Example 3 (unknown):
```unknown
PetscDrawScalePopup()
```

---

## PetscDrawTriangle#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawTriangle/

**Contents:**
- PetscDrawTriangle#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

draws a triangle onto a drawable.

draw - the drawing context

x1 - coordinate of the first vertex

y_1 - coordinate of the first vertex

x2 - coordinate of the second vertex

y2 - coordinate of the second vertex

x3 - coordinate of the third vertex

y3 - coordinate of the third vertex

c1 - color of the first vertex

c2 - color of the second vertex

c3 - color of the third vertext

PetscDraw, PetscDrawLine(), PetscDrawRectangle(), PetscDrawEllipse(), PetscDrawMarker(), PetscDrawPoint(), PetscDrawArrow()

src/sys/classes/draw/interface/dtri.c

PetscDrawTriangle_Image() in src/sys/classes/draw/impls/image/drawimage.c PetscDrawTriangle_Null() in src/sys/classes/draw/impls/null/drawnull.c PetscDrawTriangle_TikZ() in src/sys/classes/draw/impls/tikz/tikz.c PetscDrawTriangle_Win32() in src/sys/classes/draw/impls/win32/win32draw.c PetscDrawTriangle_X() in src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawTriangle(PetscDraw draw, PetscReal x1, PetscReal y_1, PetscReal x2, PetscReal y2, PetscReal x3, PetscReal y3, int c1, int c2, int c3)
```

Example 2 (unknown):
```unknown
PetscDrawLine()
```

Example 3 (unknown):
```unknown
PetscDrawRectangle()
```

Example 4 (unknown):
```unknown
PetscDrawEllipse()
```

---

## PetscDrawType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawType/

**Contents:**
- PetscDrawType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PetscDraw implementation, for example PETSC_DRAW_X is for X Windows.

PetscDrawSetType(), PetscDraw, PetscViewer, PetscDrawCreate(), PetscDrawRegister()

include/petscdrawtypes.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_DRAW_X
```

Example 2 (unknown):
```unknown
typedef const char *PetscDrawType;
#define PETSC_DRAW_X     "x"
#define PETSC_DRAW_NULL  "null"
#define PETSC_DRAW_WIN32 "win32"
#define PETSC_DRAW_TIKZ  "tikz"
#define PETSC_DRAW_IMAGE "image"
```

Example 3 (unknown):
```unknown
PetscDrawSetType()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscDrawUtilitySetCmap#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawUtilitySetCmap/

**Contents:**
- PetscDrawUtilitySetCmap#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#

Populate the RGB entries of a colormap from a named palette, honoring options-database overrides for the colormap name, reversal, and brightness.

colormap - the name of the colormap (e.g. "hue", "gray", "jet", "viridis"), or NULL/empty for the default

mapsize - the number of colormap entries to fill

R - the red channel of length mapsize

G - the green channel of length mapsize

B - the blue channel of length mapsize

-draw_cmap name - select the colormap by name

-draw_cmap_reverse - reverse the colormap

-draw_cmap_brighten value - brighten (positive) or darken (negative) the colormap; value must be in (-1, 1)

PetscDraw, PetscDrawUtilitySetGamma()

src/sys/classes/draw/utils/cmap.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscDrawUtilitySetCmap(const char colormap[], int mapsize, unsigned char R[], unsigned char G[], unsigned char B[])
```

Example 2 (unknown):
```unknown
PetscDrawUtilitySetGamma()
```

---

## PetscDrawUtilitySetGamma#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawUtilitySetGamma/

**Contents:**
- PetscDrawUtilitySetGamma#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Set the monitor gamma-correction value used by the drawing colormap utilities.

g - the gamma value; a typical value is 2.0

PetscDraw, PetscDrawUtilitySetCmap()

src/sys/classes/draw/utils/cmap.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscDrawUtilitySetGamma(PetscReal g)
```

Example 2 (unknown):
```unknown
PetscDrawUtilitySetCmap()
```

---

## PetscDrawViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewFromOptions/

**Contents:**
- PetscDrawViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscDraw from the option database

A - the PetscDraw context

obj - Optional object

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscDraw, PetscDrawView, PetscObjectViewFromOptions(), PetscDrawCreate()

src/sys/classes/draw/interface/drawreg.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawViewFromOptions(PetscDraw A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscDrawView
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscDrawViewPortsCreateRect#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsCreateRect/

**Contents:**
- PetscDrawViewPortsCreateRect#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#

Splits a window into smaller view ports. Each processor shares all the viewports. The number of views in the x- and y-directions is specified.

draw - the drawing context

nx - the number of x divisions

ny - the number of y divisions

newports - a PetscDrawViewPorts context (C structure)

PetscDrawSplitViewPort(), PetscDrawSetViewPort(), PetscDrawViewPortsSet(), PetscDrawViewPortsDestroy(), PetscDrawViewPorts

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawViewPortsCreateRect(PetscDraw draw, PetscInt nx, PetscInt ny, PetscDrawViewPorts *newports[])
```

Example 2 (unknown):
```unknown
PetscDrawViewPorts
```

Example 3 (unknown):
```unknown
PetscDrawSplitViewPort()
```

Example 4 (unknown):
```unknown
PetscDrawSetViewPort()
```

---

## PetscDrawViewPortsCreate#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsCreate/

**Contents:**
- PetscDrawViewPortsCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Fortran Note#
- See Also#
- Level#
- Location#

Splits a window into smaller view ports. Each processor shares all the viewports.

draw - the drawing context

nports - the number of ports

newports - a PetscDrawViewPorts context (C structure)

-draw_ports - display multiple fields in the same window with PetscDrawPorts() instead of in separate windows

No Fortran support since PetscDrawViewPorts is a C struct

PetscDrawSplitViewPort(), PetscDrawSetViewPort(), PetscDrawViewPortsSet(), PetscDrawViewPortsDestroy()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawViewPortsCreate(PetscDraw draw, PetscInt nports, PetscDrawViewPorts *newports[])
```

Example 2 (unknown):
```unknown
PetscDrawViewPorts
```

Example 3 (unknown):
```unknown
PetscDrawViewPorts
```

Example 4 (unknown):
```unknown
PetscDrawSplitViewPort()
```

---

## PetscDrawViewPortsDestroy#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsDestroy/

**Contents:**
- PetscDrawViewPortsDestroy#
- Synopsis#
- Input Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#

frees a PetscDrawViewPorts object

Collective on the PetscDraw inside ports

ports - the PetscDrawViewPorts object

PetscDrawViewPorts, PetscDrawSplitViewPort(), PetscDrawSetViewPort(), PetscDrawViewPortsSet(), PetscDrawViewPortsCreate()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawViewPorts
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawViewPortsDestroy(PetscDrawViewPorts *ports)
```

Example 3 (unknown):
```unknown
PetscDrawViewPorts
```

Example 4 (unknown):
```unknown
PetscDrawViewPorts
```

---

## PetscDrawViewPortsSet#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewPortsSet/

**Contents:**
- PetscDrawViewPortsSet#
- Synopsis#
- Input Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#

sets a draw object to use a particular subport

Logically Collective on the PetscDraw inside ports

ports - the PetscDrawViewPorts object

port - the port number, from 0 to nports-1

PetscDrawViewPorts, PetscDrawSplitViewPort(), PetscDrawSetViewPort(), PetscDrawViewPortsDestroy(), PetscDrawViewPortsCreate()

src/sys/classes/draw/interface/dviewp.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
PetscErrorCode PetscDrawViewPortsSet(PetscDrawViewPorts *ports, PetscInt port)
```

Example 2 (unknown):
```unknown
PetscDrawViewPorts
```

Example 3 (unknown):
```unknown
PetscDrawViewPorts
```

Example 4 (unknown):
```unknown
PetscDrawSplitViewPort()
```

---

## PetscDrawViewPorts#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawViewPorts/

**Contents:**
- PetscDrawViewPorts#
- Synopsis#
- See Also#
- Level#
- Location#

Object representing subwindows in a PetscDraw object

PetscDraw, PetscDrawViewPortsCreate(), PetscDrawViewPortsSet()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  PetscInt   nports;
  PetscReal *xl;
  PetscReal *xr;
  PetscReal *yl;
  PetscReal *yr;
  PetscDraw  draw;
  PetscReal  port_xl, port_yl, port_xr, port_yr; /* original port of parent PetscDraw */
} PetscDrawViewPorts;
```

Example 2 (unknown):
```unknown
PetscDrawViewPortsCreate()
```

Example 3 (unknown):
```unknown
PetscDrawViewPortsSet()
```

---

## PetscDrawView#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawView/

**Contents:**
- PetscDrawView#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Prints the PetscDraw data structure.

indraw - the PetscDraw context

viewer - visualization context

See PetscDrawSetFromOptions() for options database keys

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

PetscDraw, PetscViewerASCIIOpen(), PetscViewer

src/sys/classes/draw/interface/drawreg.c

PetscDrawView_Image() in src/sys/classes/draw/impls/image/drawimage.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscDrawView(PetscDraw indraw, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscDrawZoom#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDrawZoom/

**Contents:**
- PetscDrawZoom#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Allows one to provide a function that gets called for zooming in on a drawing using the mouse buttons

draw - the window where the graph will be made.

func - users function that draws the graphic

ctx - pointer to any application required data

draw - the PetscDraw object to zoom on

ctx - the context for the zooming operation

PetscDraw, PetscDrawCreate()

src/sys/classes/draw/utils/zoom.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdraw.h"  
PetscErrorCode PetscDrawZoom(PetscDraw draw, PetscErrorCode (*func)(PetscDraw draw, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscDrawCreate()
```

---

## PetscDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscDraw/

**Contents:**
- PetscDraw#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object for graphics, often represents a window on the screen

PetscDrawCreate(), PetscDrawSetType(), PetscDrawType

include/petscdrawtypes.h

src/ts/tutorials/ex5.c src/ts/tutorials/ex2.c src/ts/tutorials/ex4.c src/ts/tutorials/ex21.c src/ksp/ksp/tutorials/ex68.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c src/ksp/ksp/tutorials/ex69.c

_p_PetscDraw in include/petsc/private/drawimpl.h PetscDraw_TikZ in src/sys/classes/draw/impls/tikz/tikz.c PetscDraw_X in src/sys/classes/draw/impls/x/ximpl.h

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDraw *PetscDraw;
```

Example 2 (unknown):
```unknown
PetscDrawCreate()
```

Example 3 (unknown):
```unknown
PetscDrawSetType()
```

Example 4 (unknown):
```unknown
PetscDrawType
```

---

## PetscHDF5DataTypeToPetscDataType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscHDF5DataTypeToPetscDataType/

**Contents:**
- PetscHDF5DataTypeToPetscDataType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Finds the PETSc name of a datatype from its HDF5 name

htype - the HDF5 datatype (for example H5T_NATIVE_DOUBLE, …)

ptype - the PETSc datatype name (for example PETSC_DOUBLE)

Viewers: Looking at PETSc Objects, PetscDataType

src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewerhdf5.h" 
PetscErrorCode PetscHDF5DataTypeToPetscDataType(hid_t htype, PetscDataType *ptype)
```

Example 2 (unknown):
```unknown
H5T_NATIVE_DOUBLE
```

Example 3 (unknown):
```unknown
PETSC_DOUBLE
```

Example 4 (unknown):
```unknown
PetscDataType
```

---

## PetscHDF5IntCast#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscHDF5IntCast/

**Contents:**
- PetscHDF5IntCast#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Safely cast a nonnegative PetscInt to an HDF5 hsize_t, raising an error on overflow or negative input

Not Collective; No Fortran Support

a - the PetscInt value to convert

b - on output, the value as an hsize_t

Used internally by PETSc’s HDF5 viewer routines when computing dataset dimensions and offsets.

PetscViewerHDF5, PetscIntCast(), PetscMPIIntCast()

include/petscviewerhdf5.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
static inline PetscErrorCode PetscHDF5IntCast(PetscInt a, hsize_t *b)
```

Example 2 (unknown):
```unknown
PetscViewerHDF5
```

Example 3 (unknown):
```unknown
PetscIntCast()
```

Example 4 (unknown):
```unknown
PetscMPIIntCast()
```

---

## PetscMatlabEngineCreate#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineCreate/

**Contents:**
- PetscMatlabEngineCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Creates a MATLAB engine object

comm - a separate MATLAB engine is started for each process in the communicator

host - name of machine where MATLAB engine is to be run (usually NULL)

mengine - the resulting object

-matlab_engine_graphics - allow the MATLAB engine to display graphics

-matlab_engine_host - hostname, machine to run the MATLAB engine on

-info - print out all requests to MATLAB and all if its responses (for debugging)

If a host string is passed in, any MATLAB scripts that need to run in the engine must be available via MATLABPATH on that machine.

One must ./configure PETSc with --with-matlab [-with-matlab-dir=matlab_root_directory] to use this capability

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineCreate(MPI_Comm comm, const char host[], PetscMatlabEngine *mengine)
```

Example 2 (unknown):
```unknown
./configure
```

Example 3 (sass):
```sass
--with-matlab [-with-matlab-dir=matlab_root_directory]
```

Example 4 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

---

## PetscMatlabEngineDestroy#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineDestroy/

**Contents:**
- PetscMatlabEngineDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Shuts down a MATLAB engine.

PetscMatlabEngineCreate(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineDestroy(PetscMatlabEngine *v)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineCreate()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEngineEvaluate#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineEvaluate/

**Contents:**
- PetscMatlabEngineEvaluate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Evaluates a string in MATLAB

mengine - the MATLAB engine

string - format as in a printf()

Run the PETSc program with -info to always have printed back MATLAB’s response to the string evaluation

If the string utilizes a MATLAB script that needs to run in the engine, the script must be available via MATLABPATH on that machine.

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineCreate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

src/snes/tutorials/ex5.c src/vec/vec/tutorials/ex31.c src/snes/tutorials/ex55.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (lua):
```lua
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineEvaluate(PetscMatlabEngine mengine, const char string[], ...)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEngineGetArray#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGetArray/

**Contents:**
- PetscMatlabEngineGetArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Gets a variable from MATLAB into an array

mengine - the MATLAB engine

m - the x dimension of the array

n - the y dimension of the array

array - the array (represented in one dimension), much be large enough to hold all the data

name - the name of the array

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineCreate(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGet(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineGetArray(PetscMatlabEngine mengine, int m, int n, PetscScalar array[], const char name[])
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineCreate()
```

---

## PetscMatlabEngineGetOutput#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGetOutput/

**Contents:**
- PetscMatlabEngineGetOutput#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets a string buffer where the MATLAB output is printed

mengine - the MATLAB engine

string - buffer where MATLAB output is printed

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineCreate(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

src/vec/vec/tutorials/ex31.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineGetOutput(PetscMatlabEngine mengine, const char *string[])
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEngineGet#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngineGet/

**Contents:**
- PetscMatlabEngineGet#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets a variable from MATLAB into a PETSc object.

mengine - the MATLAB engine

obj - the PETSc object, for example a Vec

Mats transferred between PETSc and MATLAB and vis versa are transposed in the other space (this is because MATLAB uses compressed column format and PETSc uses compressed row format)

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineCreate(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

src/snes/tutorials/ex5.c src/vec/vec/tutorials/ex31.c src/snes/tutorials/ex55.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEngineGet(PetscMatlabEngine mengine, PetscObject obj)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineCreate()
```

---

## PetscMatlabEnginePrintOutput#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePrintOutput/

**Contents:**
- PetscMatlabEnginePrintOutput#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

prints the output from MATLAB to an ASCII file

mengine - the MATLAB engine

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEngineCreate(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEnginePrintOutput(PetscMatlabEngine mengine, FILE *fd)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEnginePut()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEnginePutArray#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePutArray/

**Contents:**
- PetscMatlabEnginePutArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Puts an array into the MATLAB space, treating it as a Fortran style (column major ordering) array. For parallel objects, each processors part is put in a separate MATLAB process.

mengine - the MATLAB engine

m - the x dimension of the array

n - the y dimension of the array

array - the array (represented in one dimension)

name - the name of the array

PetscMatlabEngineDestroy(), PetscMatlabEngineCreate(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePut(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEnginePutArray(PetscMatlabEngine mengine, int m, int n, const PetscScalar array[], const char name[])
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEngineCreate()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEnginePut#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEnginePut/

**Contents:**
- PetscMatlabEnginePut#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Puts a PETSc object, such as a Mat or Vec into the MATLAB space. For parallel objects, each processor’s part is put in a separate MATLAB process.

mengine - the MATLAB engine

obj - the PETSc object, for example Vec

Mats transferred between PETSc and MATLAB and vis versa are transposed in the other space (this is because MATLAB uses compressed column format and PETSc uses compressed row format)

PetscMatlabEngineDestroy(), PetscMatlabEngineCreate(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PETSC_MATLAB_ENGINE_(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine

src/sys/classes/matlabengine/matlab.c

src/snes/tutorials/ex5.c src/vec/vec/tutorials/ex31.c src/snes/tutorials/ex55.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscErrorCode PetscMatlabEnginePut(PetscMatlabEngine mengine, PetscObject obj)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 3 (unknown):
```unknown
PetscMatlabEngineCreate()
```

Example 4 (unknown):
```unknown
PetscMatlabEngineGet()
```

---

## PetscMatlabEngine#

**URL:** https://petsc.org/release/manualpages/Matlab/PetscMatlabEngine/

**Contents:**
- PetscMatlabEngine#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Object used to communicate with MATLAB

Mats transferred between PETSc and MATLAB and vis versa are transposed in the other space (this is because MATLAB uses compressed column format and PETSc uses compressed row format)

One must ./configure PETSc with --with-matlab [-with-matlab-dir=matlab_root_directory] to use this capability

PetscMatlabEngineCreate(), PetscMatlabEngineDestroy(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEnginePrintOutput(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PETSC_MATLAB_ENGINE_(), PETSC_MATLAB_ENGINE_SELF, PETSC_MATLAB_ENGINE_WORLD

include/petscmatlab.h

_p_PetscMatlabEngine in src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscMatlabEngine *PetscMatlabEngine;
```

Example 2 (unknown):
```unknown
./configure
```

Example 3 (sass):
```sass
--with-matlab [-with-matlab-dir=matlab_root_directory]
```

Example 4 (unknown):
```unknown
PetscMatlabEngineCreate()
```

---

## PetscMonitorCompare#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscMonitorCompare/

**Contents:**
- PetscMonitorCompare#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks if two monitors are identical; if they are then it destroys the new one

nmon - The new monitor

nmctx - The new monitor context, or NULL

nmdestroy - The new monitor context destroy function, or NULL, see PetscCtxDestroyFn for its calling sequence

mon - The old monitor

mctx - The old monitor context, or NULL

mdestroy - The old monitor context destroy function, or NULL, see PetscCtxDestroyFn for its calling sequence

identical - PETSC_TRUE if the monitors are the same

Viewers: Looking at PETSc Objects, DMMonitorSetFromOptions(), KSPMonitorSetFromOptions(), SNESMonitorSetFromOptions(), PetscCtxDestroyFn

src/sys/classes/viewer/interface/viewers.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscMonitorCompare(PetscErrorCode (*nmon)(void), void *nmctx, PetscCtxDestroyFn *nmdestroy, PetscErrorCode (*mon)(void), void *mctx, PetscCtxDestroyFn *mdestroy, PetscBool *identical)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 4 (unknown):
```unknown
DMMonitorSetFromOptions()
```

---

## PetscObjectViewSAWs#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscObjectViewSAWs/

**Contents:**
- PetscObjectViewSAWs#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

View the base portion of any object with an SAWs viewer

obj - the PetscObject variable. It must be cast with a (PetscObject), for example, PetscObjectSetName((PetscObject)mat,name);

viewer - the SAWs viewer

The object must have already been named before calling this routine since naming an object can be collective.

Currently this is called only on MPI rank 0 of PETSC_COMM_WORLD

Viewers: Looking at PETSc Objects, PetscViewer, PetscObject, PetscObjectSetName()

src/sys/classes/viewer/impls/ams/amsopen.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"    
#include "petscviewersaws.h"    
PetscErrorCode PetscObjectViewSAWs(PetscObject obj, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
PetscObjectSetName
```

---

## PetscOpenSocket#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOpenSocket/

**Contents:**
- PetscOpenSocket#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

handles connected to an open port where someone is waiting.

hostname - for example www.mcs.anl.gov

portnum - for example 80

t - the socket number

Use close() to close the socket connection

Use read() or PetscHTTPRequest() to read from the socket

PetscSocketListen(), PetscSocketEstablish(), PetscHTTPRequest(), PetscHTTPSConnect()

src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"  
PetscErrorCode PetscOpenSocket(const char hostname[], int portnum, int *t)
```

Example 2 (unknown):
```unknown
PetscHTTPRequest()
```

Example 3 (unknown):
```unknown
PetscSocketListen()
```

Example 4 (unknown):
```unknown
PetscSocketEstablish()
```

---

## PetscOptionsCreateViewers#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsCreateViewers/

**Contents:**
- PetscOptionsCreateViewers#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Create multiple viewers from a comma-separated list in the options database

comm - the communicator to own the viewers

options - options database, use NULL for default global database

pre - the string to prepend to the name or NULL

name - the options database name that will be checked for

n_max - on input: the maximum number of viewers; on output: the number of viewers in the comma-separated list

viewers - an array to hold at least n_max PetscViewers, or NULL if not needed; on output: if not NULL, the first n_max entries are initialized PetscViewers

formats - an array to hold at least n_max PetscViewerFormats, or NULL if not needed; on output: if not NULL, the first n_max entries are valid PetscViewewFormats

set - PETSC_TRUE if found, else PETSC_FALSE

See PetscOptionsCreateViewer() for how the format strings for the viewers are interpreted.

Use PetscViewerDestroy() on each viewer, otherwise a memory leak will occur.

If PETSc is configured with --with-viewfromoptions=0 this function always returns with n_max of 0 and set of PETSC_FALSE

Viewers: Looking at PETSc Objects, PetscOptionsCreateViewer()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsCreateViewers(MPI_Comm comm, PetscOptions options, const char pre[], const char name[], PetscInt *n_max, PetscViewer viewers[], PetscViewerFormat formats[], PetscBool *set)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerFormat
```

---

## PetscOptionsCreateViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsCreateViewer/

**Contents:**
- PetscOptionsCreateViewer#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a viewer appropriate for the type indicated by the user

comm - the communicator to own the viewer

options - options database, use NULL for default global database

pre - the string to prepend to the name or NULL

name - the options database name that will be checked for

viewer - the viewer, pass NULL if not needed

format - the PetscViewerFormat requested by the user, pass NULL if not needed

set - PETSC_TRUE if found, else PETSC_FALSE

The argument has the following form

where all parts are optional, but you need to include the colon to access the next part. The mode argument must a valid PetscFileMode, i.e. read, write, append, update, or append_update. For example, to read from an HDF5 file, use

If no value is provided ascii:stdout is used

ascii[:[filename][:[format][:append]]] - defaults to stdout - format can be one of ascii_info, ascii_info_detail, or ascii_matlab, for example ascii::ascii_info prints just the information about the object not all details unless :append is given filename opens in write mode, overwriting what was already there

binary[:[filename][:[format][:append]]] - defaults to the file binaryoutput

draw[:drawtype[:filename]] - for example, draw:tikz, draw:tikz:figure.tex or draw:x

socket[:port] - defaults to the standard output port

saws[:communicatorname] - publishes object to the Scientific Application Webserver (SAWs)

You can control whether calls to this function create a viewer (or return early with *set of PETSC_FALSE) with PetscOptionsPushCreateViewerOff(). This is useful if calling many small subsolves, in which case XXXViewFromOptions can take an appreciable fraction of the runtime.

If PETSc is configured with --with-viewfromoptions=0 this function always returns with *set of PETSC_FALSE

This routine is thread-safe for accessing predefined PetscViewers like PETSC_VIEWER_STDOUT_SELF but not for accessing files by name.

Viewers: Looking at PETSc Objects, PetscViewerDestroy(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList(), PetscOptionsPushCreateViewerOff(), PetscOptionsPopCreateViewerOff(), PetscOptionsCreateViewerOff()

src/sys/classes/viewer/interface/viewreg.c

src/dm/impls/plex/tutorials/ex19.c src/sys/classes/viewer/tutorials/ex2.c src/snes/tutorials/ex36.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsCreateViewer(MPI_Comm comm, PetscOptions options, const char pre[], const char name[], PetscViewer *viewer, PetscViewerFormat *format, PetscBool *set)
```

Example 2 (unknown):
```unknown
PetscViewerFormat
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (sass):
```sass
type:filename:format:filemode
```

---

## PetscOptionsGetCreateViewerOff#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsGetCreateViewerOff/

**Contents:**
- PetscOptionsGetCreateViewerOff#
- Synopsis#
- Output Parameter#
- See Also#
- Level#
- Location#

do PetscOptionsCreateViewer(), PetscOptionsViewer(), and PetscOptionsCreateViewers() return viewers

flg - whether viewers are returned.

Viewers: Looking at PETSc Objects, PetscOptionsCreateViewer(), PetscOptionsPushCreateViewerOff(), PetscOptionsPopCreateViewerOff()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscOptionsCreateViewer()
```

Example 2 (unknown):
```unknown
PetscOptionsViewer()
```

Example 3 (unknown):
```unknown
PetscOptionsCreateViewers()
```

Example 4 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsGetCreateViewerOff(PetscBool *flg)
```

---

## PetscOptionsHelpPrintedCheck#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsHelpPrintedCheck/

**Contents:**
- PetscOptionsHelpPrintedCheck#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks if a particular pre, name pair has previous been entered (meaning the help message was printed)

hp - the object used to manage tracking what help messages have been printed

pre - the prefix part of the string, many be NULL

name - the string to look for (cannot be NULL)

found - PETSC_TRUE if the string was already set

PetscOptionsHelpPrintedCreate()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsHelpPrintedCheck(PetscOptionsHelpPrinted hp, const char *pre, const char *name, PetscBool *found)
```

Example 2 (unknown):
```unknown
PetscOptionsHelpPrintedCreate()
```

---

## PetscOptionsHelpPrintedCreate#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsHelpPrintedCreate/

**Contents:**
- PetscOptionsHelpPrintedCreate#
- Synopsis#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates an object used to manage tracking which help messages have been printed so they will not be printed again.

hp - the created object

PetscOptionsHelpPrintedCheck(), PetscOptionsHelpPrintChecked()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsHelpPrintedCreate(PetscOptionsHelpPrinted *hp)
```

Example 2 (unknown):
```unknown
PetscOptionsHelpPrintedCheck()
```

Example 3 (unknown):
```unknown
PetscOptionsHelpPrintChecked()
```

---

## PetscOptionsHelpPrintedDestroy#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsHelpPrintedDestroy/

**Contents:**
- PetscOptionsHelpPrintedDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys the object used to track which help messages have already been printed

hp - pointer to the PetscOptionsHelpPrinted object to destroy; set to NULL on return

PetscOptionsHelpPrintedCreate(), PetscOptionsHelpPrintedCheck()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsHelpPrintedDestroy(PetscOptionsHelpPrinted *hp)
```

Example 2 (unknown):
```unknown
PetscOptionsHelpPrinted
```

Example 3 (unknown):
```unknown
PetscOptionsHelpPrintedCreate()
```

Example 4 (unknown):
```unknown
PetscOptionsHelpPrintedCheck()
```

---

## PetscOptionsPopCreateViewerOff#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsPopCreateViewerOff/

**Contents:**
- PetscOptionsPopCreateViewerOff#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

reset whether PetscOptionsCreateViewer() returns a viewer.

See PetscOptionsPushCreateViewerOff()

Viewers: Looking at PETSc Objects, PetscOptionsCreateViewer(), PetscOptionsPushCreateViewerOff()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscOptionsCreateViewer()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsPopCreateViewerOff(void)
```

Example 3 (unknown):
```unknown
PetscOptionsPushCreateViewerOff()
```

Example 4 (unknown):
```unknown
PetscOptionsCreateViewer()
```

---

## PetscOptionsPushCreateViewerOff#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsPushCreateViewerOff/

**Contents:**
- PetscOptionsPushCreateViewerOff#
- Synopsis#
- Input Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

sets if PetscOptionsCreateViewer(), PetscOptionsViewer(), and PetscOptionsCreateViewers() return viewers.

flg - PETSC_TRUE to turn off viewer creation, PETSC_FALSE to turn it on.

Calling XXXViewFromOptions in an inner loop can be expensive. This can appear, for example, when using many small subsolves. Call this function to control viewer creation in PetscOptionsCreateViewer(), thus removing the expensive XXXViewFromOptions calls.

Instead of using this approach, the calls to PetscOptionsCreateViewer() can be moved into XXXSetFromOptions()

Viewers: Looking at PETSc Objects, PetscOptionsCreateViewer(), PetscOptionsPopCreateViewerOff()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscOptionsCreateViewer()
```

Example 2 (unknown):
```unknown
PetscOptionsViewer()
```

Example 3 (unknown):
```unknown
PetscOptionsCreateViewers()
```

Example 4 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscOptionsPushCreateViewerOff(PetscBool flg)
```

---

## PetscOptionsViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscOptionsViewer/

**Contents:**
- PetscOptionsViewer#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

From a PetscOptionsBegin()/PetscOptionsEnd() block, read a viewer specification from the options database and create the requested PetscViewer

opt - the option name, for example -vec_view

text - help string shown by -help

man - manual page name (the name of an .html file under the PETSc doc tree)

viewer - the PetscViewer created, or NULL if the option was not given

format - the PetscViewerFormat requested by the option, or the default

set - PETSC_TRUE if the user supplied the option, PETSC_FALSE otherwise

Must be called between PetscOptionsBegin() and PetscOptionsEnd(); expands to a call to the internal PetscOptionsViewer_Private(), which has access to the current PetscOptionsObject. Destroy viewer with PetscViewerDestroy() when finished.

PetscOptionsCreateViewer(), PetscOptionsBegin(), PetscOptionsEnd(), PetscViewer, PetscViewerFormat, PetscViewerDestroy()

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscOptionsBegin()
```

Example 2 (unknown):
```unknown
PetscOptionsEnd()
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (cpp):
```cpp
#include <petscviewer.h>
PetscErrorCode PetscOptionsViewer(const char opt[], const char text[], const char man[], PetscViewer *viewer, PetscViewerFormat *format, PetscBool *set)
```

---

## PetscSysFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscSysFinalizePackage/

**Contents:**
- PetscSysFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the system library portion of PETSc. It is called from PetscFinalize().

PetscSysInitializePackage(), PetscFinalize()

src/sys/classes/viewer/interface/dlregispetsc.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscSysFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscSysInitializePackage()
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## PetscSysInitializePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscSysInitializePackage/

**Contents:**
- PetscSysInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function initializes everything in the system library portion of PETSc. It is called from PetscDLLibraryRegister_petsc() when using dynamic libraries, and in the call to PetscInitialize() when using shared or static libraries.

This function never needs to be called by PETSc users.

PetscSysFinalizePackage(), PetscInitialize()

src/sys/classes/viewer/interface/dlregispetsc.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister_petsc()
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscSysInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscSysFinalizePackage()
```

---

## PetscViewerADIOSOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerADIOSOpen/

**Contents:**
- PetscViewerADIOSOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Opens a file for ADIOS input/output.

comm - MPI communicator

adiosv - PetscViewer for ADIOS input/output to use with the specified file

This PetscViewer should be destroyed with PetscViewerDestroy().

PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), PetscViewerHDF5Open(), VecView(), MatView(), VecLoad(), PetscViewerSetType(), PetscViewerFileSetMode(), PetscViewerFileSetName(), MatLoad(), PetscFileMode, PetscViewer

src/sys/classes/viewer/impls/adios/adios.c

src/vec/vec/tutorials/ex10.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerADIOSOpen(MPI_Comm comm, const char name[], PetscFileMode type, PetscViewer *adiosv)
```

Example 2 (bash):
```bash
FILE_MODE_WRITE - create new file for binary output
    FILE_MODE_READ - open existing file for binary input
    FILE_MODE_APPEND - open existing file for binary output
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSCVIEWERADIOS#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERADIOS/

**Contents:**
- PETSCVIEWERADIOS#
- See Also#
- Level#
- Location#

A viewer that writes to an ADIOS file

PetscViewerADIOSOpen(), PetscViewerStringSPrintf(), PetscViewerSocketOpen(), PetscViewerDrawOpen(), PETSCVIEWERSOCKET, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PETSCVIEWERDRAW, PETSCVIEWERSTRING, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/adios/adios.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerADIOSOpen()
```

Example 2 (unknown):
```unknown
PetscViewerStringSPrintf()
```

Example 3 (unknown):
```unknown
PetscViewerSocketOpen()
```

Example 4 (unknown):
```unknown
PetscViewerDrawOpen()
```

---

## PetscViewerAndFormatCreate#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerAndFormatCreate/

**Contents:**
- PetscViewerAndFormatCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a PetscViewerAndFormat struct.

vf - viewer and format object

This increases the reference count of the viewer.

Use PetscViewerAndFormatDestroy() to free the struct

This is used as the context variable for many of the TS, SNES, and KSP monitor functions

This construct exists because it allows one to keep track of the use of a PetscViewerFormat without requiring the format in the viewer to be permanently changed.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerAndFormat, PetscViewerFormat, PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDrawOpen(), PetscViewerAndFormatDestroy()

src/sys/classes/viewer/interface/view.c

src/ksp/ksp/tutorials/ex2f.F90 src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/ts/tutorials/ex7.c src/snes/tutorials/ex30.c src/ts/tutorials/ex12.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerAndFormat
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerAndFormatCreate(PetscViewer viewer, PetscViewerFormat format, PetscViewerAndFormat **vf)
```

Example 3 (unknown):
```unknown
PetscViewerAndFormatDestroy()
```

Example 4 (unknown):
```unknown
PetscViewerFormat
```

---

## PetscViewerAndFormatDestroy#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerAndFormatDestroy/

**Contents:**
- PetscViewerAndFormatDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a PetscViewerAndFormat struct created with PetscViewerAndFormatCreate()

vf - the PetscViewerAndFormat to be destroyed.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerAndFormat, PetscViewerFormat, PetscViewerAndFormatCreate(), PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDrawOpen()

src/sys/classes/viewer/interface/view.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex2f.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerAndFormat
```

Example 2 (unknown):
```unknown
PetscViewerAndFormatCreate()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerAndFormatDestroy(PetscViewerAndFormat **vf)
```

Example 4 (unknown):
```unknown
PetscViewerAndFormat
```

---

## PetscViewerAndFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerAndFormat/

**Contents:**
- PetscViewerAndFormat#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

A struct that contains both a PetscViewer and a PetscViewerFormat plus some optional situation-dependent data

Used by most monitor functions including, for example, KSPMonitorResidual()

Viewers: Looking at PETSc Objects, PetscViewerType, PETSCVIEWERASCII, PetscViewerCreate(), PetscViewerSetType(), VecView(), VecViewFromOptions(), PetscObjectView(), PetscViewerFormat, PetscViewer, PetscViewerAndFormatCreate(), PetscViewerAndFormatDestroy(), KSPMonitorResidual()

include/petscviewer.h

src/ksp/ksp/tutorials/ex2f.F90 src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/ts/tutorials/ex7.c src/snes/tutorials/ex30.c src/ts/tutorials/ex12.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerFormat
```

Example 3 (unknown):
```unknown
typedef struct {
  PetscViewer        viewer;
  PetscViewerFormat  format;
  PetscInt           view_interval;
  void              *data;
  PetscCtxDestroyFn *data_destroy;
} PetscViewerAndFormat;
```

Example 4 (unknown):
```unknown
KSPMonitorResidual()
```

---

## PetscViewerAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerAppendOptionsPrefix/

**Contents:**
- PetscViewerAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for PetscViewer options in the database during PetscViewerSetFromOptions().

viewer - the PetscViewer context

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerGetOptionsPrefix(), PetscViewerSetOptionsPrefix()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerSetFromOptions()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerAppendOptionsPrefix(PetscViewer viewer, const char prefix[])
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerASCIIAddTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIAddTab/

**Contents:**
- PetscViewerASCIIAddTab#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Add to the number of times a PETSCVIEWERASCII viewer tabs before printing

Not Collective, but only first processor in set has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

tabs - number of tabs

PetscViewerASCIIPushTab() and PetscViewerASCIIPopTab() are the preferred usage

Viewers: Looking at PETSc Objects, PETSCVIEWERASCII, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPushTab()

src/sys/classes/viewer/impls/ascii/filev.c

src/snes/tutorials/ex6.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIAddTab(PetscViewer viewer, PetscInt tabs)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscViewerASCIIPushTab()
```

---

## PetscViewerASCIIGetPointer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetPointer/

**Contents:**
- PetscViewerASCIIGetPointer#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Extracts the file pointer from an ASCII PetscViewer.

Not Collective, depending on the viewer the value may be meaningless except for process 0 of the viewer; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerASCIIOpen()

For the standard PETSCVIEWERASCII the value is valid only on MPI rank 0 of the viewer

Viewers: Looking at PETSc Objects, PETSCVIEWERASCII, PetscViewerASCIIOpen(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerCreate(), PetscViewerASCIIPrintf(), PetscViewerASCIISynchronizedPrintf(), PetscViewerFlush()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIGetPointer(PetscViewer viewer, FILE **fd)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerASCIIGetStderr#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetStderr/

**Contents:**
- PetscViewerASCIIGetStderr#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERASCII PetscViewer shared by all MPI processes in a communicator that prints to stderr. Error returning version of PETSC_VIEWER_STDERR_()

comm - the MPI communicator to share the PetscViewer

Use PetscViewerDestroy() to destroy it

This should be used in all PETSc source code instead of PETSC_VIEWER_STDERR_() since it allows error checking

Viewers: Looking at PETSc Objects, PetscViewerASCIIGetStdout(), PETSC_VIEWER_DRAW_(), PetscViewerASCIIOpen(), PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDERR_WORLD, PETSC_VIEWER_STDERR_SELF

src/sys/classes/viewer/impls/ascii/vcreatea.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDERR_()
```

Example 4 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerASCIIGetStderr(MPI_Comm comm, PetscViewer *viewer)
```

---

## PetscViewerASCIIGetStdout#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetStdout/

**Contents:**
- PetscViewerASCIIGetStdout#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Creates a PETSCVIEWERASCII PetscViewer shared by all processes in a communicator that prints to stdout. Error returning version of PETSC_VIEWER_STDOUT_()

comm - the MPI communicator to share the PetscViewer

Use PetscViewerDestroy() to destroy it

This should be used in all PETSc source code instead of PETSC_VIEWER_STDOUT_() since it allows error checking

Viewers: Looking at PETSc Objects, PetscViewerASCIIGetStderr(), PETSC_VIEWER_DRAW_(), PetscViewerASCIIOpen(), PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF

src/sys/classes/viewer/impls/ascii/filev.c

src/snes/tutorials/ex6.c src/ts/tutorials/ex14.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_()
```

Example 4 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIGetStdout(MPI_Comm comm, PetscViewer *viewer)
```

---

## PetscViewerASCIIGetTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIGetTab/

**Contents:**
- PetscViewerASCIIGetTab#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the number of tabs used by PetscViewer.

Not Collective, meaningful on first processor only; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

tabs - number of tabs

Viewers: Looking at PETSc Objects, PETSCVIEWERASCII, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIISetTab(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPushTab()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIGetTab(PetscViewer viewer, PetscInt *tabs)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PETSCVIEWERASCII
```

---

## PetscViewerASCIIOpenWithFileUnit#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIOpenWithFileUnit/

**Contents:**
- PetscViewerASCIIOpenWithFileUnit#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

opens a PETSCVIEWERASCII to write to a Fortran IO unit

comm - the MPI_Comm to share the viewer

unit - the unit number

ierr - the error code

PetscViewerDestroy() does not close the unit for this PetscViewer

Only for Fortran, use PetscViewerASCIIOpenWithFILE() for C

PetscViewerASCIISetFileUnit(), PetscViewerASCIISetFILE(), PETSCVIEWERASCII, PetscViewerASCIIOpenWithFILE()

src/sys/classes/viewer/impls/ascii/filev.c

src/sys/tutorials/ex10f.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (cpp):
```cpp
#include <petscviewer.h>
void PetscViewerASCIIOpenWithFileUnit((MPI_Fint comm, integer unit, PetscViewer viewer, PetscErrorCode ierr)
```

Example 3 (unknown):
```unknown
PetscViewerDestroy()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerASCIIOpenWithFILE#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIOpenWithFILE/

**Contents:**
- PetscViewerASCIIOpenWithFILE#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#

Given an open file creates an PETSCVIEWERASCII viewer that prints to it.

comm - the communicator

fd - the FILE pointer

viewer - the PetscViewer to use with the specified file

This PetscViewer can be destroyed with PetscViewerDestroy(), but the fd will NOT be closed.

If a multiprocessor communicator is used (such as PETSC_COMM_WORLD), then only the first processor in the group uses the file. All other processors send their data to the first processor to print.

Use PetscViewerASCIIOpenWithFileUnit()

Viewers: Looking at PETSc Objects, MatView(), VecView(), PetscViewerDestroy(), PetscViewerBinaryOpen(), PetscViewerASCIIOpenWithFileUnit(), PetscViewerASCIIGetPointer(), PetscViewerPushFormat(), PETSC_VIEWER_STDOUT_, PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, PetscViewerASCIIOpen(), PetscViewerASCIISetFILE(), PETSCVIEWERASCII

src/sys/classes/viewer/impls/ascii/vcreatea.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerASCIIOpenWithFILE(MPI_Comm comm, FILE *fd, PetscViewer *viewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerASCIIOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIOpen/

**Contents:**
- PetscViewerASCIIOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Opens an ASCII file for writing as a PETSCVIEWERASCII PetscViewer.

comm - the communicator

viewer - the PetscViewer to use with the specified file

This routine only opens files for writing. To open a ASCII file as a PetscViewer for reading use the sequence

This PetscViewer can be destroyed with PetscViewerDestroy().

The MPI communicator used here must match that used by the object viewed. For example if the Mat was created with a PETSC_COMM_WORLD, then viewer must be created with PETSC_COMM_WORLD

As shown below, PetscViewerASCIIOpen() is useful in conjunction with MatView() and VecView()

When called with NULL, stdout, or stderr this does not return the same communicator as PetscViewerASCIIGetStdout() or PetscViewerASCIIGetStderr() but that is ok.

Viewers: Looking at PETSc Objects, MatView(), VecView(), PetscViewerDestroy(), PetscViewerBinaryOpen(), PetscViewerASCIIRead(), PETSCVIEWERASCII, PetscViewerASCIIGetPointer(), PetscViewerPushFormat(), PETSC_VIEWER_STDOUT_, PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, PetscViewerASCIIGetStdout(), PetscViewerASCIIGetStderr()

src/sys/classes/viewer/impls/ascii/vcreatea.c

src/ksp/ksp/tutorials/ex55.c src/ksp/ksp/tutorials/ex2f.F90 src/ksp/ksp/tutorials/ex56.c src/ksp/ksp/tutorials/ex72.c src/snes/tutorials/ex1f.F90 src/snes/tutorials/ex70.c src/ksp/ksp/tutorials/ex54.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/ksp/ksp/tutorials/ex76.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerASCIIOpen(MPI_Comm comm, const char name[], PetscViewer *viewer)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerASCIIPopSynchronized#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPopSynchronized/

**Contents:**
- PetscViewerASCIIPopSynchronized#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Undoes most recent PetscViewerASCIIPushSynchronized() for this viewer

viewer - obtained with PetscViewerASCIIOpen()

See documentation of PetscViewerASCIISynchronizedPrintf() for more details how the synchronized output should be done properly.

Viewers: Looking at PETSc Objects, PetscViewerASCIIPushSynchronized(), PetscViewerASCIISynchronizedPrintf(), PetscViewerFlush(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType()

src/sys/classes/viewer/impls/ascii/filev.c

src/vec/is/sf/tutorials/ex1.c src/dm/tutorials/swarm_ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerASCIIPushSynchronized()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIPopSynchronized(PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscViewerASCIISynchronizedPrintf()
```

---

## PetscViewerASCIIPopTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPopTab/

**Contents:**
- PetscViewerASCIIPopTab#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Removes one tab from the amount that PetscViewerASCIIPrintf() lines are tabbed that was provided by PetscViewerASCIIPushTab()

Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

Viewers: Looking at PETSc Objects, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIPushTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer()

src/sys/classes/viewer/impls/ascii/filev.c

src/ts/tutorials/ex14.c src/vec/vec/utils/tagger/tutorials/ex1.c src/tao/constrained/tutorials/ex1.c src/vec/is/sf/tutorials/ex1.c src/dm/label/tutorials/ex1f90.F90 src/dm/label/tutorials/ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerASCIIPrintf()
```

Example 2 (unknown):
```unknown
PetscViewerASCIIPushTab()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIPopTab(PetscViewer viewer)
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerASCIIPrintf#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPrintf/

**Contents:**
- PetscViewerASCIIPrintf#
- Synopsis#
- Input Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Prints to a file, only from the first processor in the PetscViewer of type PETSCVIEWERASCII

Not Collective, but only the first MPI rank in the viewer has any effect

viewer - obtained with PetscViewerASCIIOpen()

format - the usual printf() format string

The call sequence is PetscViewerASCIIPrintf(PetscViewer, character(*), int ierr). That is, you can only pass a single character string from Fortran.

Viewers: Looking at PETSc Objects, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerASCIIPushTab(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPushSynchronized()

src/sys/classes/viewer/impls/ascii/filev.c

src/snes/tutorials/ex6.c src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/ksp/ksp/tutorials/ex68.c src/snes/tutorials/ex70.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/ksp/ksp/tutorials/ex69.c src/sys/classes/viewer/tutorials/ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 3 (lua):
```lua
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIPrintf(PetscViewer viewer, const char format[], ...)
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerASCIIPushSynchronized#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPushSynchronized/

**Contents:**
- PetscViewerASCIIPushSynchronized#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Allows calls to PetscViewerASCIISynchronizedPrintf() for this viewer

viewer - obtained with PetscViewerASCIIOpen()

See documentation of PetscViewerASCIISynchronizedPrintf() for more details how the synchronized output should be done properly.

Viewers: Looking at PETSc Objects, PetscViewerASCIISynchronizedPrintf(), PetscViewerFlush(), PetscViewerASCIIPopSynchronized(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType()

src/sys/classes/viewer/impls/ascii/filev.c

src/vec/is/sf/tutorials/ex1.c src/dm/tutorials/swarm_ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerASCIISynchronizedPrintf()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIPushSynchronized(PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscViewerASCIISynchronizedPrintf()
```

---

## PetscViewerASCIIPushTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIPushTab/

**Contents:**
- PetscViewerASCIIPushTab#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Adds one more tab to the amount that PetscViewerASCIIPrintf() lines are tabbed.

Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

Viewers: Looking at PETSc Objects, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer()

src/sys/classes/viewer/impls/ascii/filev.c

src/ts/tutorials/ex14.c src/vec/vec/utils/tagger/tutorials/ex1.c src/tao/constrained/tutorials/ex1.c src/vec/is/sf/tutorials/ex1.c src/dm/label/tutorials/ex1f90.F90 src/dm/label/tutorials/ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerASCIIPrintf()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIPushTab(PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscPrintf()
```

---

## PetscViewerASCIIRead#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIRead/

**Contents:**
- PetscViewerASCIIRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Reads from a PETSCVIEWERASCII file

Only MPI rank 0 in the PetscViewer may call this

viewer - the PETSCVIEWERASCII viewer

data - location to write the data, treated as an array of type indicated by datatype

num - number of items of data to read

dtype - type of data to read

count - number of items of data actually read, or NULL

Viewers: Looking at PETSc Objects, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), PetscViewerCreate(), PetscViewerFileSetMode(), PetscViewerFileSetName(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer, PetscViewerBinaryRead()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIRead(PetscViewer viewer, void *data, PetscInt num, PetscInt *count, PetscDataType dtype)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERASCII
```

---

## PetscViewerASCIISetFileUnit#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISetFileUnit/

**Contents:**
- PetscViewerASCIISetFileUnit#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#

sets the PETSCVIEWERASCII PetscViewer to write to a Fortran IO unit

unit - the unit number

ierr - the error code

PetscViewerDestroy() does not close the unit for this PetscViewer

Only for Fortran, use PetscViewerASCIISetFILE() for C

PetscViewerASCIISetFILE(), PETSCVIEWERASCII, PetscViewerASCIIOpenWithFileUnit(), PetscViewerASCIIStdoutSetFileUnit()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (cpp):
```cpp
#include <petscviewer.h>
void PetscViewerASCIISetFileUnit(PetscViewer viewer, PetscInt unit, PetscErrorCode ierr)
```

Example 4 (unknown):
```unknown
PetscViewerDestroy()
```

---

## PetscViewerASCIISetFILE#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISetFILE/

**Contents:**
- PetscViewerASCIISetFILE#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Given an open file sets the PETSCVIEWERASCII viewer to use the file for output

viewer - the PetscViewer to use with the specified file

fd - the FILE pointer

This PetscViewer can be destroyed with PetscViewerDestroy(), but the fd will NOT be closed.

If a multiprocessor communicator is used (such as PETSC_COMM_WORLD), then only the first processor in the group uses the file. All other processors send their data to the first processor to print.

Use PetscViewerASCIISetFileUnit()

MatView(), VecView(), PetscViewerDestroy(), PetscViewerBinaryOpen(), PetscViewerASCIISetFileUnit(), PetscViewerASCIIGetPointer(), PetscViewerPushFormat(), PETSC_VIEWER_STDOUT_, PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, PetscViewerASCIIOpen(), PetscViewerASCIIOpenWithFILE(), PETSCVIEWERASCII

src/sys/classes/viewer/impls/ascii/vcreatea.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerASCIISetFILE(PetscViewer viewer, FILE *fd)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerASCIISetTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISetTab/

**Contents:**
- PetscViewerASCIISetTab#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Causes PetscViewer to tab in a number of times before printing

Not Collective, but only first processor in set has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

tabs - number of tabs

PetscViewerASCIIPushTab() and PetscViewerASCIIPopTab() are the preferred usage

Viewers: Looking at PETSc Objects, PETSCVIEWERASCII, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIGetTab(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPushTab()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIISetTab(PetscViewer viewer, PetscInt tabs)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscViewerASCIIPushTab()
```

---

## PetscViewerASCIIStdoutSetFileUnit#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIStdoutSetFileUnit/

**Contents:**
- PetscViewerASCIIStdoutSetFileUnit#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- Developer Note#
- See Also#
- Level#
- Location#

sets PETSC_VIEWER_STDOUT_() to write to a Fortran IO unit

unit - the unit number

ierr - the error code

Can be called before PetscInitialize()

Immediately changes the output for all PETSC_VIEWER_STDOUT_() viewers

This may not work currently with some viewers that (improperly) use the fd directly instead of PetscViewerASCIIPrintf()

With this option, for example, -log_options results will be saved to the Fortran file

Any process may call this but only the unit passed on the first process is used

PetscViewerASCIIWORLDSetFilename() and PetscViewerASCIIWORLDSetFILE() could be added

PetscViewerASCIISetFILE(), PETSCVIEWERASCII, PetscViewerASCIIOpenWithFileUnit(), PetscViewerASCIIStdoutSetFileUnit(), PETSC_VIEWER_STDOUT_(), PetscViewerASCIIGetStdout()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDOUT_()
```

Example 2 (cpp):
```cpp
#include <petscviewer.h>
void PetscViewerASCIIStdoutSetFileUnit(PetscInt unit, PetscErrorCode ierr)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_STDOUT_()
```

---

## PetscViewerASCIISubtractTab#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISubtractTab/

**Contents:**
- PetscViewerASCIISubtractTab#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Subtracts from the number of times a PETSCVIEWERASCII viewer tabs before printing

Not Collective, but only first processor in set has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

tabs - number of tabs

PetscViewerASCIIPushTab() and PetscViewerASCIIPopTab() are the preferred usage

Viewers: Looking at PETSc Objects, PETSCVIEWERASCII, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPushTab()

src/sys/classes/viewer/impls/ascii/filev.c

src/snes/tutorials/ex6.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIISubtractTab(PetscViewer viewer, PetscInt tabs)
```

Example 3 (unknown):
```unknown
PetscViewerASCIIOpen()
```

Example 4 (unknown):
```unknown
PetscViewerASCIIPushTab()
```

---

## PetscViewerASCIISynchronizedPrintf#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIISynchronizedPrintf/

**Contents:**
- PetscViewerASCIISynchronizedPrintf#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Prints synchronized output to the specified PETSCVIEWERASCII file from several processors. Output of the first processor is followed by that of the second, etc.

Not Collective, must call collective PetscViewerFlush() to get the results flushed

viewer - the PETSCVIEWERASCII PetscViewer

format - the usual printf() format string

You must have previously called PetscViewerASCIIPushSynchronized() to allow this routine to be called. Then you can do multiple independent calls to this routine.

The actual synchronized print is then done using PetscViewerFlush(). PetscViewerASCIIPopSynchronized() should be then called if we are already done with the synchronized output to conclude the “synchronized session”.

So the typical calling sequence looks like

The call sequence is PetscViewerASCIISynchronizedPrintf(PetscViewer, character(*), PetscErrorCode ierr) That is, you can only pass a single character string from Fortran.

Viewers: Looking at PETSc Objects, PetscViewerASCIIPushSynchronized(), PetscViewerFlush(), PetscViewerASCIIPopSynchronized(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType()

src/sys/classes/viewer/impls/ascii/filev.c

src/vec/is/sf/tutorials/ex1.c src/dm/tutorials/swarm_ex1.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (lua):
```lua
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIISynchronizedPrintf(PetscViewer viewer, const char format[], ...)
```

Example 3 (unknown):
```unknown
PetscViewerFlush()
```

Example 4 (unknown):
```unknown
PETSCVIEWERASCII
```

---

## PetscViewerASCIIUseTabs#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerASCIIUseTabs/

**Contents:**
- PetscViewerASCIIUseTabs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Turns on or off the use of tabs with the PETSCVIEWERASCII PetscViewer

Not Collective, but only first MPI rank in the viewer has any effect; No Fortran Support

viewer - obtained with PetscViewerASCIIOpen()

flg - PETSC_TRUE or PETSC_FALSE

Viewers: Looking at PETSc Objects, PetscPrintf(), PetscSynchronizedPrintf(), PetscViewerASCIIPrintf(), PetscViewerASCIIPopTab(), PetscViewerASCIISynchronizedPrintf(), PetscViewerASCIIPushTab(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType(), PetscViewerASCIIGetPointer()

src/sys/classes/viewer/impls/ascii/filev.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerASCIIUseTabs(PetscViewer viewer, PetscBool flg)
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PETSCVIEWERASCII#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERASCII/

**Contents:**
- PETSCVIEWERASCII#
- See Also#
- Level#
- Location#
- Examples#

A viewer that prints to stdout, stderr, or an ASCII file

Viewers: Looking at PETSc Objects, PETSC_VIEWER_STDOUT_(), PETSC_VIEWER_STDOUT_SELF, PETSC_VIEWER_STDOUT_WORLD, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERBINARY, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/ascii/filev.c

src/ts/tutorials/ex9.c src/tao/term/tutorials/ex1.c src/vec/vec/utils/tagger/tutorials/ex1.c src/sys/classes/viewer/tutorials/ex1.c src/sys/tutorials/ex7.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDOUT_()
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 4 (unknown):
```unknown
PetscViewerCreate()
```

---

## PetscViewerBinaryAddMPIIOOffset#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryAddMPIIOOffset/

**Contents:**
- PetscViewerBinaryAddMPIIOOffset#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds to the current global offset

Logically Collective; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

off - the addition to the global offset

Use PetscViewerBinaryGetMPIIOOffset() to get the value that you should pass to MPI_File_set_view() or MPI_File_{write|read}_at[_all]()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinaryGetUseMPIIO(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryGetMPIIOOffset()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryAddMPIIOOffset(PetscViewer viewer, MPI_Offset off)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerBinaryGetMPIIOOffset()
```

---

## PetscViewerBinaryGetDescriptor#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetDescriptor/

**Contents:**
- PetscViewerBinaryGetDescriptor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Extracts the file descriptor from a PetscViewer of PetscViewerType PETSCVIEWERBINARY.

Collective because it may trigger a PetscViewerSetUp() call; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

fdes - file descriptor

For writable binary PetscViewers, the descriptor will only be valid for the first processor in the communicator that shares the PetscViewer. For readable files it will only be valid on processes that have the file. If MPI rank 0 does not have the file it generates an error even if another MPI process does have the file.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer()

src/sys/classes/viewer/impls/binary/binv.c

src/vec/vec/tutorials/ex6.c src/vec/vec/tutorials/ex6f.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerType
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetDescriptor(PetscViewer viewer, int *fdes)
```

---

## PetscViewerBinaryGetFlowControl#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetFlowControl/

**Contents:**
- PetscViewerBinaryGetFlowControl#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Returns how many messages are allowed to be outstanding at the same time during parallel IO reads/writes

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

fc - the number of messages

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinarySetFlowControl()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinaryGetFlowControl_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetFlowControl(PetscViewer viewer, PetscInt *fc)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerBinaryGetInfoPointer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetInfoPointer/

**Contents:**
- PetscViewerBinaryGetInfoPointer#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Extracts the file pointer for the ASCII .info file associated with a binary file.

Not Collective; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

file - file pointer Always returns NULL if not a binary viewer

For writable binary PetscViewers, the file pointer will only be valid for the first processor in the MPI communicator that shares the PetscViewer.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetSkipInfo(), PetscViewerBinarySetSkipInfo()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinaryGetInfoPointer_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetInfoPointer(PetscViewer viewer, FILE **file)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerBinaryGetMPIIODescriptor#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetMPIIODescriptor/

**Contents:**
- PetscViewerBinaryGetMPIIODescriptor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Extracts the MPI IO file descriptor from a PetscViewer.

Not Collective; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

fdes - file descriptor

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinaryGetUseMPIIO(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryGetMPIIOOffset()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetMPIIODescriptor(PetscViewer viewer, MPI_File *fdes)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerBinaryOpen()
```

---

## PetscViewerBinaryGetMPIIOOffset#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetMPIIOOffset/

**Contents:**
- PetscViewerBinaryGetMPIIOOffset#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the current global offset that should be passed to MPI_File_set_view() or MPI_File_{write|read}_at[_all]()

Not Collective; No Fortran Support

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

off - the current global offset

Use PetscViewerBinaryAddMPIIOOffset() to increase this value after you have written a view.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinaryGetUseMPIIO(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryAddMPIIOOffset()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MPI_File_set_view()
```

Example 2 (markdown):
```markdown
MPI_File_{write|read}_at[_all]()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetMPIIOOffset(PetscViewer viewer, MPI_Offset *off)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerBinaryGetSkipHeader#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipHeader/

**Contents:**
- PetscViewerBinaryGetSkipHeader#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

checks whether to write a header with size information on output, or just raw data

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

skip - PETSC_TRUE means do not write header

This must be called after PetscViewerSetType()

Returns PETSC_FALSE for PETSCSOCKETVIEWER, you cannot skip the header for it.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySkipInfo(), PetscViewerBinarySetSkipHeader()

src/sys/classes/viewer/impls/binary/binv.c

src/dm/tutorials/ex15.c

PetscViewerBinaryGetSkipHeader_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerBinaryGetSkipHeader_Socket() in src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetSkipHeader(PetscViewer viewer, PetscBool *skip)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewerBinaryGetSkipInfo#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipInfo/

**Contents:**
- PetscViewerBinaryGetSkipInfo#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

check if viewer wrote a .info file

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

skip - PETSC_TRUE implies the .info file was not generated

This must be called after PetscViewerSetType()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySetSkipOptions(), PetscViewerBinarySetSkipInfo(), PetscViewerBinaryGetInfoPointer()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinaryGetSkipInfo_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetSkipInfo(PetscViewer viewer, PetscBool *skip)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerBinaryGetSkipOptions#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetSkipOptions/

**Contents:**
- PetscViewerBinaryGetSkipOptions#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

checks if viewer uses the PETSc options database when loading objects

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

skip - PETSC_TRUE means do not use

This must be called after PetscViewerSetType()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySkipInfo(), PetscViewerBinarySetSkipOptions()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinaryGetSkipOptions_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetSkipOptions(PetscViewer viewer, PetscBool *skip)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerBinaryGetUseMPIIO#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryGetUseMPIIO/

**Contents:**
- PetscViewerBinaryGetUseMPIIO#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns PETSC_TRUE if the binary viewer uses MPI-IO.

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen(); must be a PETSCVIEWERBINARY

use - PETSC_TRUE if MPI-IO is being used

If MPI-IO is not available, this function will always return PETSC_FALSE

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryGetMPIIOOffset()

src/sys/classes/viewer/impls/binary/binv.c

src/dm/tutorials/ex15.c

PetscViewerBinaryGetUseMPIIO_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryGetUseMPIIO(PetscViewer viewer, PetscBool *use)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerBinaryOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryOpen/

**Contents:**
- PetscViewerBinaryOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Opens a file for binary input/output.

comm - MPI communicator

mode - open mode of file

viewer - PetscViewer for binary input/output to use with the specified file

-viewer_binary_filename name - name of file to use

-viewer_binary_skip_info - true to skip opening an info file

-viewer_binary_skip_options - true to not use options database while creating viewer

-viewer_binary_skip_header - true to skip output object headers to the file

-viewer_binary_mpiio - true to use MPI-IO for input and output to the file (more scalable for large problems)

This PetscViewer should be destroyed with PetscViewerDestroy().

For reading files, the filename may begin with ftp:// or http:// and/or end with .gz; in this case file is brought over and uncompressed.

For creating files, if the file name ends with .gz it is automatically compressed when closed.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer, PetscViewerBinaryRead(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryGetUseMPIIO(), PetscViewerBinaryGetMPIIOOffset()

src/sys/classes/viewer/impls/binary/binv.c

src/ksp/pc/tutorials/ex4.c src/mat/tutorials/ex1.c src/ksp/ksp/tutorials/ex72.c src/ksp/ksp/tutorials/ex10.c src/ksp/ksp/tutorials/ex75f.F90 src/ksp/ksp/tutorials/ex76f.F90 src/mat/tutorials/ex16.c src/snes/tutorials/ex30.c src/ksp/ksp/tutorials/ex77f.F90 src/mat/tutorials/ex12.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryOpen(MPI_Comm comm, const char name[], PetscFileMode mode, PetscViewer *viewer)
```

Example 2 (bash):
```bash
FILE_MODE_WRITE - create new file for binary output
    FILE_MODE_READ - open existing file for binary input
    FILE_MODE_APPEND - open existing file for binary output
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerDestroy()
```

---

## PetscViewerBinaryReadAll#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryReadAll/

**Contents:**
- PetscViewerBinaryReadAll#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

reads from a binary file from all MPI processes, each rank receives its own portion of the data

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

count - local number of items of data to read

start - local start, can be PETSC_DETERMINE

total - global number of items of data to read, can be PETSC_DETERMINE

dtype - type of data to read

data - location of data, treated as an array of type indicated by dtype

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryRead(), PetscViewerBinaryWriteAll()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryReadAll(PetscViewer viewer, void *data, PetscCount count, PetscCount start, PetscCount total, PetscDataType dtype)
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE
```

---

## PetscViewerBinaryReadStringArray#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryReadStringArray/

**Contents:**
- PetscViewerBinaryReadStringArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

reads a binary file an array of strings to all MPI processes

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

data - location of the array of strings

The array of strings must NULL terminated

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer, PetscViewerBinaryRead()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryReadStringArray(PetscViewer viewer, char ***data)
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerBinaryRead#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryRead/

**Contents:**
- PetscViewerBinaryRead#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Reads from a binary file, all processors get the same result

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

num - number of items of data to read

dtype - type of data to read

data - location of the read data, treated as an array of the type indicated by dtype

count - number of items of data actually read, or NULL.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryRead(PetscViewer viewer, void *data, PetscInt num, PetscInt *count, PetscDataType dtype)
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerBinarySetFlowControl#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetFlowControl/

**Contents:**
- PetscViewerBinarySetFlowControl#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets how many messages are allowed to be outstanding at the same time during parallel IO reads/writes

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

fc - the number of messages, defaults to 256 if this function was not called

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetInfoPointer(), PetscViewerBinaryGetFlowControl()

src/sys/classes/viewer/impls/binary/binv.c

src/vec/vec/tutorials/ex10.c

PetscViewerBinarySetFlowControl_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySetFlowControl(PetscViewer viewer, PetscInt fc)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerBinarySetSkipHeader#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipHeader/

**Contents:**
- PetscViewerBinarySetSkipHeader#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

do not write a header with size information on output, just raw data

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

skip - PETSC_TRUE means do not write header

-viewer_binary_skip_header (true|false) - true means do not write header

This must be called after PetscViewerSetType()

If this option is selected, the output file cannot be read with the XXXLoad() such as VecLoad()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySkipInfo(), PetscViewerBinaryGetSkipHeader()

src/sys/classes/viewer/impls/binary/binv.c

src/dm/tutorials/ex15.c

PetscViewerBinarySetSkipHeader_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerBinarySetSkipHeader_Socket() in src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySetSkipHeader(PetscViewer viewer, PetscBool skip)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerBinarySetSkipInfo#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipInfo/

**Contents:**
- PetscViewerBinarySetSkipInfo#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Binary file will not have .info file created with it

viewer - PetscViewer context, obtained from PetscViewerCreate()

skip - PETSC_TRUE implies the .info file will not be generated

-viewer_binary_skip_info - true indicates do not generate .info file

This must be called after PetscViewerSetType(). If you use PetscViewerBinaryOpen() then you can only skip the info file with the -viewer_binary_skip_info flag. To use the function you must open the viewer with PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinarySkipInfo().

The .info file contains meta information about the data in the binary file, for example the block size if it was set for a vector or matrix.

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySetSkipOptions(), PetscViewerBinaryGetSkipOptions(), PetscViewerBinaryGetSkipInfo(), PetscViewerBinaryGetInfoPointer()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinarySetSkipInfo_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySetSkipInfo(PetscViewer viewer, PetscBool skip)
```

Example 2 (unknown):
```unknown
PetscViewerCreate()
```

Example 3 (unknown):
```unknown
PetscViewerSetType()
```

Example 4 (unknown):
```unknown
PetscViewerBinaryOpen()
```

---

## PetscViewerBinarySetSkipOptions#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetSkipOptions/

**Contents:**
- PetscViewerBinarySetSkipOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

do not use values in the PETSc options database when loading objects

viewer - PetscViewer context, obtained from PetscViewerBinaryOpen()

skip - PETSC_TRUE means do not use the options from the options database

-viewer_binary_skip_options (true|false) - true means do not use the options from the options database

This must be called after PetscViewerSetType()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySkipInfo(), PetscViewerBinaryGetSkipOptions()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerBinarySetSkipOptions_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySetSkipOptions(PetscViewer viewer, PetscBool skip)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerBinarySetUseMPIIO#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySetUseMPIIO/

**Contents:**
- PetscViewerBinarySetUseMPIIO#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets a binary viewer to use MPI-IO for reading/writing. Must be called before PetscViewerFileSetName()

viewer - the PetscViewer; must be a PETSCVIEWERBINARY

use - PETSC_TRUE means MPI-IO will be used

-viewer_binary_mpiio (true|false) - flag for using MPI-IO

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen(), PetscViewerBinaryGetUseMPIIO()

src/sys/classes/viewer/impls/binary/binv.c

src/dm/tutorials/ex15.c

PetscViewerBinarySetUseMPIIO_Binary() in src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerFileSetName()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySetUseMPIIO(PetscViewer viewer, PetscBool use)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerBinarySkipInfo#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinarySkipInfo/

**Contents:**
- PetscViewerBinarySkipInfo#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Binary file will not have .info file created with it

viewer - PetscViewer context, obtained from PetscViewerCreate()

-viewer_binary_skip_info - true indicates do not generate .info file

This must be called after PetscViewerSetType(). If you use PetscViewerBinaryOpen() then you can only skip the info file with the -viewer_binary_skip_info flag. To use the function you must open the viewer with PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinarySkipInfo().

The .info files contains meta information about the data in the binary file, for example the block size if it was set for a vector or matrix.

This routine is deprecated, use PetscViewerBinarySetSkipInfo()

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinaryGetDescriptor(), PetscViewerBinarySetSkipOptions(), PetscViewerBinaryGetSkipOptions(), PetscViewerBinaryGetSkipInfo()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinarySkipInfo(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerCreate()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerBinaryWriteAll#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWriteAll/

**Contents:**
- PetscViewerBinaryWriteAll#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

writes to a binary file from all MPI processes, each rank writes its own portion of the data

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

data - location of data

count - local number of items of data to write, treated as an array of type indicated by dtype

start - local start, can be PETSC_DETERMINE

total - global number of items of data to write, can be PETSC_DETERMINE

dtype - type of data to write

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerBinaryOpen(), PetscViewerBinarySetUseMPIIO(), PetscViewerBinaryReadAll()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryWriteAll(PetscViewer viewer, const void *data, PetscCount count, PetscCount start, PetscCount total, PetscDataType dtype)
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE
```

---

## PetscViewerBinaryWriteStringArray#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWriteStringArray/

**Contents:**
- PetscViewerBinaryWriteStringArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

writes to a binary file, only from the first MPI rank, an array of strings

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

data - location of the array of strings

The array of strings must be NULL terminated

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer, PetscViewerBinaryRead()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryWriteStringArray(PetscViewer viewer, const char *const data[])
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerBinaryWrite#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerBinaryWrite/

**Contents:**
- PetscViewerBinaryWrite#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

writes to a binary file, only from the first MPI rank

Collective; No Fortran Support

viewer - the PETSCVIEWERBINARY viewer

data - location of data, treated as an array of the type indicated by dtype

count - number of items of data to write

dtype - type of data to write

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscViewerBinaryGetDescriptor(), PetscDataType, PetscViewerBinaryGetInfoPointer(), PetscFileMode, PetscViewer, PetscViewerBinaryRead()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerBinaryWrite(PetscViewer viewer, const void *data, PetscInt count, PetscDataType dtype)
```

Example 2 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PETSCVIEWERBINARY#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERBINARY/

**Contents:**
- PETSCVIEWERBINARY#
- See Also#
- Level#
- Location#
- Examples#

A viewer that saves to binary files

Viewers: Looking at PETSc Objects, PetscViewerBinaryOpen(), PETSC_VIEWER_STDOUT_(), PETSC_VIEWER_STDOUT_SELF, PETSC_VIEWER_STDOUT_WORLD, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PETSCVIEWERDRAW, PETSCVIEWERSOCKET, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType(), PetscViewerBinaryGetUseMPIIO(), PetscViewerBinarySetUseMPIIO()

src/sys/classes/viewer/impls/binary/binv.c

src/ksp/ksp/tutorials/ex43.c src/mat/tutorials/ex10.c src/dm/tutorials/ex15.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_()
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

---

## PetscViewerCGNSGetSolutionIndex#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionIndex/

**Contents:**
- PetscViewerCGNSGetSolutionIndex#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Get index of solution

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

solution_id - Index of the solution id

By default, solution_id is set to -1 to mean the last solution available in the file

PETSCVIEWERCGNS, PetscViewerCGNSSetSolutionIndex(), PetscViewerCGNSGetSolutionInfo()

src/sys/classes/viewer/impls/cgns/cgnsv.c

src/dm/impls/plex/tutorials/ex15.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSGetSolutionIndex(PetscViewer viewer, PetscInt *solution_id)
```

Example 2 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERCGNS
```

---

## PetscViewerCGNSGetSolutionIteration#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionIteration/

**Contents:**
- PetscViewerCGNSGetSolutionIteration#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets the solution iteration for the FlowSolution of the viewer

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

iteration - Solution iteration of the FlowSolution_t node

set - Whether the time data is in the file

Reads data from a DataArray named IterationValues under a BaseIterativeData_t node

PETSCVIEWERCGNS, PetscViewer, PetscViewerCGNSGetSolutionTime(), PetscViewerCGNSSetSolutionIndex(), PetscViewerCGNSGetSolutionIndex(), PetscViewerCGNSGetSolutionName()

src/sys/classes/viewer/impls/cgns/cgnsv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSGetSolutionIteration(PetscViewer viewer, PetscInt *iteration, PetscBool *set)
```

Example 2 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
IterationValues
```

---

## PetscViewerCGNSGetSolutionName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionName/

**Contents:**
- PetscViewerCGNSGetSolutionName#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets name of FlowSolution of the viewer

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

name - Name of the FlowSolution_t node corresponding to the solution index

Currently assumes there is only one Zone in the CGNS file

PETSCVIEWERCGNS, PetscViewer, PetscViewerCGNSSetSolutionIndex(), PetscViewerCGNSGetSolutionIndex(), PetscViewerCGNSGetSolutionTime()

src/sys/classes/viewer/impls/cgns/cgnsv.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSGetSolutionName(PetscViewer viewer, const char *name[])
```

Example 2 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERCGNS
```

---

## PetscViewerCGNSGetSolutionTime#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSGetSolutionTime/

**Contents:**
- PetscViewerCGNSGetSolutionTime#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the solution time for the FlowSolution of the viewer

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

time - Solution time of the FlowSolution_t node

set - Whether the time data is in the file

Reads data from a DataArray named TimeValues under a BaseIterativeData_t node

PETSCVIEWERCGNS, PetscViewer, PetscViewerCGNSGetSolutionIteration(), PetscViewerCGNSSetSolutionIndex(), PetscViewerCGNSGetSolutionIndex(), PetscViewerCGNSGetSolutionName()

src/sys/classes/viewer/impls/cgns/cgnsv.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSGetSolutionTime(PetscViewer viewer, PetscReal *time, PetscBool *set)
```

Example 2 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
BaseIterativeData_t
```

---

## PetscViewerCGNSOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSOpen/

**Contents:**
- PetscViewerCGNSOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Opens a file for CGNS input/output.

comm - MPI communicator

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

PETSCVIEWERCGNS, PetscViewer, PetscViewerPushFormat(), PetscViewerDestroy(), DMLoad(), PetscFileMode, PetscViewerSetType(), PetscViewerFileSetMode(), PetscViewerFileSetName()

src/sys/classes/viewer/impls/cgns/cgnsv.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSOpen(MPI_Comm comm, const char name[], PetscFileMode type, PetscViewer *viewer)
```

Example 2 (bash):
```bash
FILE_MODE_WRITE - create new file for binary output
    FILE_MODE_READ - open existing file for binary input
    FILE_MODE_APPEND - open existing file for binary output
```

Example 3 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerCGNSSetSolutionIndex#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCGNSSetSolutionIndex/

**Contents:**
- PetscViewerCGNSSetSolutionIndex#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set index of solution

viewer - PETSCVIEWERCGNS PetscViewer for CGNS input/output to use with the specified file

solution_id - Index of the solution id, or -1 for the last solution on the file

By default, solution_id is set to -1 to mean the last solution available in the file. If the file contains a FlowSolutionPointers node, then that array is indexed to determine which FlowSolution_t node to read from. Otherwise, solution_id indexes the total available FlowSolution_t nodes in the file.

This solution index is used by VecLoad() to determine which solution to load from the file

PETSCVIEWERCGNS, PetscViewerCGNSGetSolutionIndex(), PetscViewerCGNSGetSolutionInfo()

src/sys/classes/viewer/impls/cgns/cgnsv.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscdmplex.h"   
PetscErrorCode PetscViewerCGNSSetSolutionIndex(PetscViewer viewer, PetscInt solution_id)
```

Example 2 (unknown):
```unknown
PETSCVIEWERCGNS
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
solution_id
```

---

## PETSCVIEWERCGNS#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERCGNS/

**Contents:**
- PETSCVIEWERCGNS#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

A viewer for CGNS files

-viewer_cgns_batch_size SIZE - set max number of output sequence times to write per batch

If the filename contains an integer format character, the CGNS viewer will created a batched output sequence. For example, one could use -ts_monitor_solution cgns:flow-%d.cgns. This is desirable if one wants to limit file sizes or if the job might crash/be killed by a resource manager before exiting cleanly.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), VecView(), DMView(), PetscViewerFileSetName(), PetscViewerFileSetMode(), TSSetFromOptions()

src/sys/classes/viewer/impls/cgns/cgnsv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_monitor_solution cgns:flow-%d.cgns
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerCreate()
```

Example 4 (unknown):
```unknown
PetscViewerFileSetName()
```

---

## PetscViewerCheckReadable#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCheckReadable/

**Contents:**
- PetscViewerCheckReadable#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Check whether the viewer can be read from, generates an error if not

viewer - the PetscViewer context

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerReadable(), PetscViewerCheckWritable(), PetscViewerCreate(), PetscViewerFileSetMode(), PetscViewerFileSetType()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerCheckReadable(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerReadable()
```

---

## PetscViewerCheckWritable#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCheckWritable/

**Contents:**
- PetscViewerCheckWritable#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Check whether the viewer can be written to, generates an error if not

viewer - the PetscViewer context

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerWritable(), PetscViewerCheckReadable(), PetscViewerCreate(), PetscViewerFileSetMode(), PetscViewerFileSetType()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerCheckWritable(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerWritable()
```

---

## PetscViewerCreate#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerCreate/

**Contents:**
- PetscViewerCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a viewing context. A PetscViewer represents a file, a graphical window, a Unix socket or a variety of other ways of viewing a PETSc object

comm - MPI communicator

inviewer - location to put the PetscViewer context

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerDestroy(), PetscViewerSetType(), PetscViewerType

src/sys/classes/viewer/interface/viewreg.c

src/ts/tutorials/ex11.c src/tao/term/tutorials/ex1.c src/dm/impls/plex/tutorials/ex1f90.F90 src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/dm/tutorials/ex21.c src/sys/classes/viewer/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex15.c

PetscViewerCreate_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerCreate_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerCreate_SAWs() in src/sys/classes/viewer/impls/ams/ams.c PetscViewerCreate_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerCreate_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerCreate_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerCreate_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerCreate_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c PetscViewerCreate_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerCreate_Mathematica() in src/sys/classes/viewer/impls/mathematica/mathematica.c PetscViewerCreate_Matlab() in src/sys/classes/viewer/impls/matlab/vmatlab.c PetscViewerCreate_PyVista() in src/sys/classes/viewer/impls/pyvista/pyvistaviewer.c PetscViewerCreate_Socket() in src/sys/classes/viewer/impls/socket/send.c PetscViewerCreate_String() in src/sys/classes/viewer/impls/string/stringv.c PetscViewerCreate_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerCreate_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerCreate(MPI_Comm comm, PetscViewer *inviewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDestroy#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDestroy/

**Contents:**
- PetscViewerDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys a PetscViewer.

viewer - the PetscViewer to be destroyed.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerDrawOpen()

src/sys/classes/viewer/interface/view.c

src/mat/tutorials/ex1.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/mat/tutorials/ex16.c src/snes/tutorials/ex70.c src/snes/tutorials/ex22.c src/mat/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c

PetscViewerDestroy_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerDestroy_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerDestroy_SAWs() in src/sys/classes/viewer/impls/ams/ams.c PetscViewerDestroy_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerDestroy_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerDestroy_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerDestroy_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerDestroy_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c PetscViewerDestroy_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerDestroy_Mathematica() in src/sys/classes/viewer/impls/mathematica/mathematica.c PetscViewerDestroy_Matlab() in src/sys/classes/viewer/impls/matlab/vmatlab.c PetscViewerDestroy_Socket() in src/sys/classes/viewer/impls/socket/send.c PetscViewerDestroy_String() in src/sys/classes/viewer/impls/string/stringv.c PetscViewerDestroy_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerDestroy_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerDestroy(PetscViewer *viewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawBaseAdd#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawBaseAdd/

**Contents:**
- PetscViewerDrawBaseAdd#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

add to the base integer that is added to the windownumber passed to PetscViewerDrawGetDraw()

viewer - the PetscViewer (created with PetscViewerDrawOpen())

windownumber - how much to add to the base

A PETSCVIEWERDRAW may have multiple PetscDraw subwindows, this increases the number of the subwindow that is returned with PetscViewerDrawGetDraw()

Viewers: Looking at PETSc Objects, PetscViewerDrawGetLG(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen(), PetscViewerDrawGetDraw(), PetscViewerDrawBaseSet()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
windownumber
```

Example 2 (unknown):
```unknown
PetscViewerDrawGetDraw()
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawBaseAdd(PetscViewer viewer, PetscInt windownumber)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawBaseSet#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawBaseSet/

**Contents:**
- PetscViewerDrawBaseSet#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

sets the base integer that is added to the windownumber passed to PetscViewerDrawGetDraw()

viewer - the PetscViewer (created with PetscViewerDrawOpen())

windownumber - value to set the base

A PETSCVIEWERDRAW may have multiple PetscDraw subwindows, this increases the number of the subwindow that is returned with PetscViewerDrawGetDraw()

Viewers: Looking at PETSc Objects, PetscViewerDrawGetLG(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen(), PetscViewerDrawGetDraw(), PetscViewerDrawBaseAdd()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
windownumber
```

Example 2 (unknown):
```unknown
PetscViewerDrawGetDraw()
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawBaseSet(PetscViewer viewer, PetscInt windownumber)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawClear#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawClear/

**Contents:**
- PetscViewerDrawClear#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears a PetscDraw graphic associated with a PetscViewer.

viewer - the PetscViewer

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawClear(PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawGetBounds#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetBounds/

**Contents:**
- PetscViewerDrawGetBounds#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

gets the upper and lower bounds to be used in plotting set with PetscViewerDrawSetBounds()

viewer - the PetscViewer (created with PetscViewerDrawOpen())

nbounds - number of plots that can be made with this viewer, for example the dof passed to DMDACreate()

bounds - the actual bounds, the size of this is 2*nbounds, the values are stored in the order min F_0, max F_0, min F_1, max F_1, …..

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawGetLG(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen(), PetscViewerDrawSetBounds()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerDrawSetBounds()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetBounds(PetscViewer viewer, PetscInt *nbounds, const PetscReal *bounds[])
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerDrawOpen()
```

---

## PetscViewerDrawGetDrawAxis#

**URL:** https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawAxis/

**Contents:**
- PetscViewerDrawGetDrawAxis#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns a PetscDrawAxis object from a PetscViewer object of type PETSCVIEWERDRAW. This PetscDrawAxis object may then be used to perform graphics using PetscDrawAxis commands.

viewer - the PetscViewer (created with PetscViewerDrawOpen())

windownumber - indicates which subwindow (usually 0)

drawaxis - the draw axis object

A PETSCVIEWERDRAW may have multiple PetscDraw subwindows

Viewers: Looking at PETSc Objects, PetscViewerDrawGetDraw(), PetscViewerDrawGetLG(), PetscViewerDrawOpen()

src/sys/classes/viewer/impls/draw/draw/fdrawv.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawAxis
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PetscDrawAxis
```

---

## PetscViewerDrawGetDrawLG#

**URL:** https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawLG/

**Contents:**
- PetscViewerDrawGetDrawLG#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns a PetscDrawLG object from PetscViewer object of type PETSCVIEWERDRAW. This PetscDrawLG object may then be used to perform graphics using PetscDrawLG commands.

viewer - the PetscViewer (created with PetscViewerDrawOpen())

windownumber - indicates which subwindow (usually 0)

drawlg - the draw line graph object

A PETSCVIEWERDRAW may have multiple PetscDraw subwindows

Viewers: Looking at PETSc Objects, PetscDrawLG, PetscViewerDrawGetDraw(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen()

src/sys/classes/viewer/impls/draw/draw/fdrawv.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawLG
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PetscDrawLG
```

---

## PetscViewerDrawGetDrawType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDrawType/

**Contents:**
- PetscViewerDrawGetDrawType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the underlying PetscDrawType used by a PETSCVIEWERDRAW viewer.

v - the PETSCVIEWERDRAW viewer

drawtype - the PetscDrawType currently in use

PetscViewer, PETSCVIEWERDRAW, PetscDrawType, PetscViewerDrawSetDrawType(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/draw/fdrawv.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawType
```

Example 2 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetDrawType(PetscViewer v, PetscDrawType *drawtype)
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawGetDraw#

**URL:** https://petsc.org/release/manualpages/Draw/PetscViewerDrawGetDraw/

**Contents:**
- PetscViewerDrawGetDraw#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns PetscDraw object from PETSCVIEWERDRAW PetscViewer object. This PetscDraw object may then be used to perform graphics using PetscDraw commands.

viewer - the PetscViewer (created with PetscViewerDrawOpen() of type PETSCVIEWERDRAW)

windownumber - indicates which subwindow (usually 0) to obtain

draw - the draw object

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawGetLG(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen()

src/sys/classes/viewer/impls/draw/draw/fdrawv.c

src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ts/tutorials/ex21.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c src/ts/tutorials/ex2.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetDraw(PetscViewer viewer, PetscInt windownumber, PetscDraw *draw)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawGetHold#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetHold/

**Contents:**
- PetscViewerDrawGetHold#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks if the PETSCVIEWERDRAW PetscViewer holds previous image when drawing new image

viewer - the PetscViewer

hold - indicates to hold or not

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetHold(PetscViewer viewer, PetscBool *hold)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawGetPause#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetPause/

**Contents:**
- PetscViewerDrawGetPause#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the pause value (how long to pause before an image is changed) in the PETSCVIEWERDRAW PetscViewer

viewer - the PetscViewer

pause - the pause value

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetPause(PetscViewer viewer, PetscReal *pause)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawGetTitle#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawGetTitle/

**Contents:**
- PetscViewerDrawGetTitle#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the default title used for PetscDraw windows created by a PETSCVIEWERDRAW viewer.

Not Collective; No Fortran Support

v - the PETSCVIEWERDRAW viewer

title - the window title (owned by the viewer; do not free)

PetscViewer, PETSCVIEWERDRAW, PetscViewerDrawSetTitle(), PetscViewerDrawOpen(), PetscViewerDrawSetInfo()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawGetTitle(PetscViewer v, const char *title[])
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawOpen/

**Contents:**
- PetscViewerDrawOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Opens a PetscDraw window for use as a PetscViewer with type PETSCVIEWERDRAW.

comm - communicator that will share window

display - the X display on which to open, or NULL for the local machine

title - the title to put in the title bar, or NULL for no title

x - horizontal screen coordinate of the upper left corner of window, or use PETSC_DECIDE

y - vertical screen coordinate of the upper left corner of window, or use PETSC_DECIDE

w - window width in pixels, or may use PETSC_DECIDE or PETSC_DRAW_FULL_SIZE, PETSC_DRAW_HALF_SIZE,PETSC_DRAW_THIRD_SIZE, PETSC_DRAW_QUARTER_SIZE

h - window height in pixels, or may use PETSC_DECIDE or PETSC_DRAW_FULL_SIZE, PETSC_DRAW_HALF_SIZE,PETSC_DRAW_THIRD_SIZE, PETSC_DRAW_QUARTER_SIZE

viewer - the PetscViewer

-draw_type - use x or null

-nox - Disables all x-windows output

-display name - Specifies name of machine for the X display

-geometry x,y,w,h - allows setting the window location and size

-draw_pause pause - Sets time (in seconds) that the program pauses after PetscDrawPause() has been called (0 is default, -1 implies until user input).

If you want to do graphics in this window, you must call PetscViewerDrawGetDraw() and perform the graphics on the PetscDraw object.

Format options include:

PETSC_VIEWER_DRAW_BASIC - displays with basic format

PETSC_VIEWER_DRAW_LG - displays using a line graph

Whenever indicating null character data in a Fortran code, PETSC_NULL_CHARACTER must be employed. Thus, PETSC_NULL_CHARACTER can be used for the display and title input parameters.

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscDrawCreate(), PetscViewerDestroy(), PetscViewerDrawGetDraw(), PetscViewerCreate(), PETSC_VIEWER_DRAW_, PETSC_VIEWER_DRAW_WORLD, PETSC_VIEWER_DRAW_SELF

src/sys/classes/viewer/impls/draw/drawv.c

src/snes/tutorials/ex21.c src/ts/tutorials/ex5.c src/vec/vec/tutorials/ex3f.F90 src/ts/tutorials/ex4.c src/snes/tutorials/ex3.c src/snes/tutorials/ex2.c src/vec/vec/tutorials/ex3.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c src/snes/tutorials/ex22.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawOpen(MPI_Comm comm, const char display[], const char title[], int x, int y, int w, int h, PetscViewer *viewer)
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## PetscViewerDrawResize#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawResize/

**Contents:**
- PetscViewerDrawResize#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the default width and height (in pixels) for PetscDraw windows created by a PETSCVIEWERDRAW viewer.

v - the PETSCVIEWERDRAW viewer

w - the new default window width in pixels; values less than 1 are ignored

h - the new default window height in pixels; values less than 1 are ignored

If v is not a PETSCVIEWERDRAW viewer, the call is a no-op.

PetscViewer, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawSetInfo()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawResize(PetscViewer v, int w, int h)
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawSetBounds#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetBounds/

**Contents:**
- PetscViewerDrawSetBounds#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

sets the upper and lower bounds to be used in plotting in a PETSCVIEWERDRAW PetscViewer

viewer - the PetscViewer (created with PetscViewerDrawOpen())

nbounds - number of plots that can be made with this viewer, for example the dof passed to DMDACreate()

bounds - the actual bounds, the size of this is 2*nbounds, the values are stored in the order min F_0, max F_0, min F_1, max F_1, …..

-draw_bounds minF0,maxF0,minF1,maxF1 - the lower left and upper right bounds

this determines the colors used in 2d contour plots generated with VecView() for DMDA in 2d. Any values in the vector below or above the bounds are moved to the bound value before plotting. In this way the color index from color to physical value remains the same for all plots generated with this viewer. Otherwise the color to physical value meaning changes with each new image if this is not set.

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawGetLG(), PetscViewerDrawGetAxis(), PetscViewerDrawOpen()

src/sys/classes/viewer/impls/draw/drawv.c

src/ts/tutorials/ex2.c src/ts/tutorials/ex21.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetBounds(PetscViewer viewer, PetscInt nbounds, const PetscReal *bounds)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawSetDrawType#

**URL:** https://petsc.org/release/manualpages/Draw/PetscViewerDrawSetDrawType/

**Contents:**
- PetscViewerDrawSetDrawType#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the underlying PetscDrawType used by a PETSCVIEWERDRAW viewer.

v - the PETSCVIEWERDRAW viewer

drawtype - the PetscDrawType (e.g. PETSC_DRAW_X, PETSC_DRAW_IMAGE, PETSC_DRAW_NULL)

If v is not a PETSCVIEWERDRAW viewer, the call is a no-op.

PetscViewer, PETSCVIEWERDRAW, PetscDrawType, PetscViewerDrawGetDrawType(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/draw/fdrawv.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawType
```

Example 2 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetDrawType(PetscViewer v, PetscDrawType drawtype)
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawSetHold#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetHold/

**Contents:**
- PetscViewerDrawSetHold#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Holds previous image when drawing new image in a PETSCVIEWERDRAW

viewer - the PetscViewer

hold - PETSC_TRUE indicates to hold the previous image

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetHold(PetscViewer viewer, PetscBool hold)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawSetInfo#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetInfo/

**Contents:**
- PetscViewerDrawSetInfo#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Record the default display, title, position, and size to use for PetscDraw windows created by a PETSCVIEWERDRAW viewer.

v - the PETSCVIEWERDRAW viewer

display - the X display name, or NULL for the local machine

title - the window title, or NULL

x - the horizontal screen coordinate of the upper left corner (unused; retained for API symmetry)

y - the vertical screen coordinate of the upper left corner (unused; retained for API symmetry)

w - the default window width in pixels; values less than 1 are ignored

h - the default window height in pixels; values less than 1 are ignored

If v is not a PETSCVIEWERDRAW viewer, the call is a no-op.

PetscViewer, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawSetTitle(), PetscViewerDrawResize()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetInfo(PetscViewer v, const char display[], const char title[], int x, int y, int w, int h)
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PetscViewerDrawSetPause#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetPause/

**Contents:**
- PetscViewerDrawSetPause#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a pause for each PetscDraw in the PETSCVIEWERDRAW PetscViewer

viewer - the PetscViewer

pause - the pause value

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewerDrawOpen(), PetscViewerDrawGetDraw()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetPause(PetscViewer viewer, PetscReal pause)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerDrawSetTitle#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerDrawSetTitle/

**Contents:**
- PetscViewerDrawSetTitle#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the default title used for PetscDraw windows created by a PETSCVIEWERDRAW viewer.

v - the PETSCVIEWERDRAW viewer

title - the window title, or NULL for no title

If v is not a PETSCVIEWERDRAW viewer, the call is a no-op.

PetscViewer, PETSCVIEWERDRAW, PetscViewerDrawGetTitle(), PetscViewerDrawOpen(), PetscViewerDrawSetInfo()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerDrawSetTitle(PetscViewer v, const char title[])
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## PETSCVIEWERDRAW#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERDRAW/

**Contents:**
- PETSCVIEWERDRAW#
- See Also#
- Level#
- Location#

A viewer that generates graphics, either to the screen or a file

Viewers: Looking at PETSc Objects, PetscViewerDrawOpen(), PetscViewerDrawGetDraw(), PETSC_VIEWER_DRAW_(), PETSC_VIEWER_DRAW_SELF, PETSC_VIEWER_DRAW_WORLD, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerDrawOpen()
```

Example 2 (unknown):
```unknown
PetscViewerDrawGetDraw()
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_DRAW_()
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_DRAW_SELF
```

---

## PetscViewerFileGetMode#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFileGetMode/

**Contents:**
- PetscViewerFileGetMode#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets the open mode of a file associated with a PetscViewer

viewer - the PetscViewer; must be a PETSCVIEWERBINARY, PETSCVIEWERMATLAB, PETSCVIEWERHDF5, or PETSCVIEWERASCII PetscViewer

mode - open mode of file

Viewers: Looking at PETSc Objects, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen()

src/sys/classes/viewer/impls/binary/binv.c

PetscViewerFileGetMode_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerFileGetMode_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerFileGetMode_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerFileGetMode_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerFileGetMode_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerFileGetMode_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerFileGetMode_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerFileGetMode(PetscViewer viewer, PetscFileMode *mode)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerFileGetName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFileGetName/

**Contents:**
- PetscViewerFileGetName#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Gets the name of the file the PetscViewer is using

viewer - the PetscViewer

name - the name of the file it is using

This will have no effect on viewers that are not related to files

Viewers: Looking at PETSc Objects, PetscViewerCreate(), PetscViewerSetType(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PetscViewerFileSetName()

src/sys/classes/viewer/impls/ascii/filev.c

PetscViewerFileGetName_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerFileGetName_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerFileGetName_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerFileGetName_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerFileGetName_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerFileGetName_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerFileGetName_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerFileGetName_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFileGetName(PetscViewer viewer, const char *name[])
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerCreate()
```

---

## PetscViewerFileSetMode#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFileSetMode/

**Contents:**
- PetscViewerFileSetMode#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the open mode of file

viewer - the PetscViewer; must be a PETSCVIEWERBINARY, PETSCVIEWERMATLAB, PETSCVIEWERHDF5, or PETSCVIEWERASCII PetscViewer

mode - open mode of file

Viewers: Looking at PETSc Objects, PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen()

src/sys/classes/viewer/impls/binary/binv.c

src/dm/impls/plex/tutorials/ex19.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/dm/tutorials/ex21.c src/sys/classes/viewer/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex20.c src/dm/tutorials/ex15.c

PetscViewerFileSetMode_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerFileSetMode_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerFileSetMode_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerFileSetMode_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerFileSetMode_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerFileSetMode_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerFileSetMode_Matlab() in src/sys/classes/viewer/impls/matlab/vmatlab.c PetscViewerFileSetMode_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerFileSetMode_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
PetscErrorCode PetscViewerFileSetMode(PetscViewer viewer, PetscFileMode mode)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 4 (unknown):
```unknown
PETSCVIEWERMATLAB
```

---

## PetscViewerFileSetName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFileSetName/

**Contents:**
- PetscViewerFileSetName#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the name of the file the PetscViewer should use.

viewer - the PetscViewer; for example, of type PETSCVIEWERASCII or PETSCVIEWERBINARY

name - the name of the file it should use

This will have no effect on viewers that are not related to files

Viewers: Looking at PETSc Objects, PetscViewerCreate(), PetscViewerSetType(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PetscViewerDestroy(), PetscViewerASCIIGetPointer(), PetscViewerASCIIPrintf(), PetscViewerASCIISynchronizedPrintf()

src/sys/classes/viewer/impls/ascii/filev.c

src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex1f90.F90 src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/dm/tutorials/ex21.c src/sys/classes/viewer/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex20.c src/dm/tutorials/ex15.c

PetscViewerFileSetName_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerFileSetName_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerFileSetName_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerFileSetName_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerFileSetName_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerFileSetName_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c PetscViewerFileSetName_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerFileSetName_Matlab() in src/sys/classes/viewer/impls/matlab/vmatlab.c PetscViewerFileSetName_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerFileSetName_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFileSetName(PetscViewer viewer, const char name[])
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERASCII
```

---

## PetscViewerFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFinalizePackage/

**Contents:**
- PetscViewerFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys any global objects created in PETSc viewers. It is called from PetscFinalize().

Viewers: Looking at PETSc Objects, PetscViewer, PetscFinalize(), PetscViewerInitializePackage()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## PetscViewerFlowControlEndMain#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlEndMain/

**Contents:**
- PetscViewerFlowControlEndMain#
- Synopsis#
- Input Parameter#
- Input/Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Finish a flow-controlled viewer operation on the main MPI process by signalling completion to the workers

viewer - the binary viewer

mcnt - the flow-control counter; reset to 0 and broadcast to signal completion

Broadcasting mcnt = 0 releases any worker MPI processes still waiting inside PetscViewerFlowControlEndWorker().

PetscViewer, PetscViewerFlowControlStart(), PetscViewerFlowControlStepMain(), PetscViewerFlowControlStepWorker(), PetscViewerFlowControlEndWorker()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlowControlEndMain(PetscViewer viewer, PetscInt *mcnt)
```

Example 2 (unknown):
```unknown
PetscViewerFlowControlEndWorker()
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerFlowControlStart()
```

---

## PetscViewerFlowControlEndWorker#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlEndWorker/

**Contents:**
- PetscViewerFlowControlEndWorker#
- Synopsis#
- Input Parameter#
- Input/Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Wait on a worker MPI process for the main MPI process to signal completion of a flow-controlled viewer operation

viewer - the binary viewer

mcnt - the flow-control counter; updated with values broadcast from the main MPI process until it becomes 0

Blocks in a loop of MPI_Bcast() until PetscViewerFlowControlEndMain() sends a mcnt = 0 completion signal.

PetscViewer, PetscViewerFlowControlStart(), PetscViewerFlowControlStepMain(), PetscViewerFlowControlEndMain(), PetscViewerFlowControlStepWorker()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlowControlEndWorker(PetscViewer viewer, PetscInt *mcnt)
```

Example 2 (unknown):
```unknown
MPI_Bcast()
```

Example 3 (unknown):
```unknown
PetscViewerFlowControlEndMain()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerFlowControlStart#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStart/

**Contents:**
- PetscViewerFlowControlStart#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Begin a flow-controlled viewer operation on the main MPI process

viewer - the binary viewer

mcnt - the current flow-control counter on the main MPI process

cnt - the flow-control window size (also read from the viewer)

Used together with PetscViewerFlowControlStepMain() and PetscViewerFlowControlEndMain() on the main process (rank 0), and with PetscViewerFlowControlStepWorker() and PetscViewerFlowControlEndWorker() on the other processes, to serialize I/O work through a bounded window so that all processes do not simultaneously flood the main process with data.

PetscViewer, PetscViewerFlowControlStepMain(), PetscViewerFlowControlEndMain(), PetscViewerFlowControlStepWorker(), PetscViewerFlowControlEndWorker(), PetscViewerBinaryGetFlowControl()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlowControlStart(PetscViewer viewer, PetscInt *mcnt, PetscInt *cnt)
```

Example 2 (unknown):
```unknown
PetscViewerFlowControlStepMain()
```

Example 3 (unknown):
```unknown
PetscViewerFlowControlEndMain()
```

Example 4 (unknown):
```unknown
PetscViewerFlowControlStepWorker()
```

---

## PetscViewerFlowControlStepMain#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStepMain/

**Contents:**
- PetscViewerFlowControlStepMain#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Advance the flow-control window on the main MPI process during a viewer operation

viewer - the binary viewer

i - the current MPI rank being served

cnt - the flow-control window size returned by PetscViewerFlowControlStart()

mcnt - the running flow-control counter; incremented and broadcast when i reaches it

Called on the main MPI process (rank 0) once per worker rank in a loop; when the current rank has caught up to mcnt the window is advanced by cnt and broadcast so waiting workers can proceed.

PetscViewer, PetscViewerFlowControlStart(), PetscViewerFlowControlEndMain(), PetscViewerFlowControlStepWorker(), PetscViewerFlowControlEndWorker()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlowControlStepMain(PetscViewer viewer, PetscInt i, PetscInt *mcnt, PetscInt cnt)
```

Example 2 (unknown):
```unknown
PetscViewerFlowControlStart()
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerFlowControlStart()
```

---

## PetscViewerFlowControlStepWorker#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlowControlStepWorker/

**Contents:**
- PetscViewerFlowControlStepWorker#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Wait on a worker MPI process until the flow-control window includes this rank

viewer - the binary viewer

rank - the calling MPI process rank

mcnt - the flow-control counter; updated with values broadcast from the main MPI process until it exceeds rank

Blocks in a loop of MPI_Bcast() until the main MPI process (through PetscViewerFlowControlStepMain()) advances the window past this rank, giving the worker permission to perform its I/O.

PetscViewer, PetscViewerFlowControlStart(), PetscViewerFlowControlStepMain(), PetscViewerFlowControlEndMain(), PetscViewerFlowControlEndWorker()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlowControlStepWorker(PetscViewer viewer, PetscMPIInt rank, PetscInt *mcnt)
```

Example 2 (unknown):
```unknown
MPI_Bcast()
```

Example 3 (unknown):
```unknown
PetscViewerFlowControlStepMain()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerFlush#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFlush/

**Contents:**
- PetscViewerFlush#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Flushes a PetscViewer (i.e. tries to dump all the data that has been printed through a PetscViewer).

viewer - the PetscViewer to be flushed

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerWriteable(), PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscViewerCreate(), PetscViewerDestroy(), PetscViewerSetType()

src/sys/classes/viewer/interface/flush.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/dm/tutorials/swarm_ex1.c src/vec/is/sf/tutorials/ex1.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c

PetscViewerFlush_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerFlush_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerFlush_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerFlush_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerFlush_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c PetscViewerFlush_VU() in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerFlush(PetscViewer viewer)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerFormat/

**Contents:**
- PetscViewerFormat#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#

Way a viewer presents the object

PETSC_VIEWER_DEFAULT - default format for the specific object being viewed

PETSC_VIEWER_ASCII_MATLAB - MATLAB format

PETSC_VIEWER_ASCII_DENSE - print matrix as a dense two dimensiona array

PETSC_VIEWER_ASCII_IMPL - implementation-specific format (which is in many cases the same as the default)

PETSC_VIEWER_ASCII_INFO - basic information about object

PETSC_VIEWER_ASCII_INFO_DETAIL - more detailed info about object (but still not vector or matrix entries)

PETSC_VIEWER_ASCII_COMMON - identical output format for all objects of a particular type

PETSC_VIEWER_ASCII_INDEX - (for vectors) prints the vector element number next to each vector entry

PETSC_VIEWER_ASCII_SYMMODU - print parallel vectors without indicating the MPI process ranges that own the entries

PETSC_VIEWER_ASCII_VTK - outputs the object to a VTK file (deprecated since v3.14)

PETSC_VIEWER_NATIVE - store the object to the binary file in its native format (for example, dense matrices are stored as dense), DMDA vectors are dumped directly to the file instead of being first put in the natural ordering

PETSC_VIEWER_ASCII_LATEX - output the data in LaTeX

PETSC_VIEWER_BINARY_MATLAB - output additional information that can be used to read the data into MATLAB

PETSC_VIEWER_DRAW_BASIC - views the vector with a simple 1d plot

PETSC_VIEWER_DRAW_LG - views the vector with a line graph

PETSC_VIEWER_DRAW_CONTOUR - views the vector with a contour plot

A variety of specialized formats also exist

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerType, PetscViewerPushFormat(), PetscViewerPopFormat()

include/petscviewer.h

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/tao/term/tutorials/ex1.c src/ksp/ksp/tutorials/ex76.c

src/dm/tutorials/ex7.c

src/ts/tutorials/ex9.c src/ksp/ksp/tutorials/ex55.c src/ksp/ksp/tutorials/ex56.c src/ksp/ksp/tutorials/ex34.c src/ksp/ksp/tutorials/ex54.c

src/dm/tutorials/ex22.c

src/tao/term/tutorials/ex1.c

src/dm/impls/plex/tutorials/ex19.c

src/snes/tutorials/ex1f.F90 src/ksp/ksp/tutorials/ex2f.F90

src/dm/impls/plex/tutorials/ex5.c

src/ts/tutorials/ex30.c

src/ksp/ksp/tutorials/ex27.c

src/ksp/ksp/tutorials/ex2f.F90 src/dm/impls/plex/tutorials/ex19.c src/ts/tutorials/ex52.c src/ts/tutorials/ex7.c src/snes/tutorials/ex30.c src/ts/tutorials/ex12.c

src/vec/vec/tutorials/ex3.c

src/ts/tutorials/ex30.c src/sys/classes/viewer/tutorials/ex2.c src/mat/tutorials/ex10.c src/snes/tutorials/ex36.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/dm/impls/plex/tutorials/ex5.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_VIEWER_DEFAULT,
  PETSC_VIEWER_ASCII_MATLAB,
  PETSC_VIEWER_ASCII_MATHEMATICA,
  PETSC_VIEWER_ASCII_IMPL,
  PETSC_VIEWER_ASCII_INFO,
  PETSC_VIEWER_ASCII_INFO_DETAIL,
  PETSC_VIEWER_ASCII_COMMON,
  PETSC_VIEWER_ASCII_SYMMODU,
  PETSC_VIEWER_ASCII_INDEX,
  PETSC_VIEWER_ASCII_DENSE,
  PETSC_VIEWER_ASCII_MATRIXMARKET,
  PETSC_VIEWER_ASCII_PCICE,
  PETSC_VIEWER_ASCII_PYTHON,
  PETSC_VIEWER_ASCII_FACTOR_INFO,
  PETSC_VIEWER_ASCII_LATEX,
  PETSC_VIEWER_ASCII_XML,
  PETSC_VIEWER_ASCII_FLAMEGRAPH,
  PETSC_VIEWER_ASCII_GLVIS,
  PETSC_VIEWER_ASCII_CSV,
  PETSC_VIEWER_DRAW_BASIC,
  PETSC_VIEWER_DRAW_LG,
  PETSC_VIEWER_DRAW_LG_XRANGE,
  PETSC_VIEWER_DRAW_CONTOUR,
  PETSC_VIEWER_DRAW_PORTS,
  PETSC_VIEWER_VTK_VTS,
  PETSC_VIEWER_VTK_VTR,
  PETSC_VIEWER_VTK_VTU,
  PETSC_VIEWER_BINARY_MATLAB,
  PETSC_VIEWER_NATIVE,
  PETSC_VIEWER_HDF5_PETSC,
  PETSC_VIEWER_HDF5_VIZ,
  PETSC_VIEWER_HDF5_XDMF,
  PETSC_VIEWER_HDF5_MAT,
  PETSC_VIEWER_NOFORMAT,
  PETSC_VIEWER_LOAD_BALANCE,
  PETSC_VIEWER_FAILED,
  PETSC_VIEWER_ALL
} PetscViewerFormat;
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_DEFAULT
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_ASCII_MATLAB
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_ASCII_DENSE
```

---

## PetscViewerGetFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGetFormat/

**Contents:**
- PetscViewerGetFormat#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the current format for PetscViewer.

viewer - the PetscViewer

See PetscViewerFormat for available values

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), MatView(), VecView(), PetscViewerType, PetscViewerPushFormat(), PetscViewerPopFormat(), PetscViewerDrawOpen(), PetscViewerSocketOpen()

src/sys/classes/viewer/interface/viewa.c

src/dm/impls/plex/tutorials/ex19.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscViewerGetFormat(PetscViewer viewer, PetscViewerFormat *format)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerFormat
```

---

## PetscViewerGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGetOptionsPrefix/

**Contents:**
- PetscViewerGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for PetscViewer options in the database during PetscViewerSetFromOptions().

viewer - the PetscViewer context

prefix - pointer to the prefix string used

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerAppendOptionsPrefix(), PetscViewerSetOptionsPrefix()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerSetFromOptions()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerGetOptionsPrefix(PetscViewer viewer, const char *prefix[])
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerGetSubViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGetSubViewer/

**Contents:**
- PetscViewerGetSubViewer#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a new PetscViewer (same type as the old) that lives on a subcommunicator of the original viewer’s communicator

viewer - the PetscViewer to be reproduced

comm - the sub communicator to use

outviewer - new PetscViewer

The output of the subviewers is synchronized against the original viewer. For example, if a viewer on two MPI processes is decomposed into two subviewers, the output from the first viewer is all printed before the output from the second viewer.

Call PetscViewerRestoreSubViewer() to destroy this PetscViewer, NOT PetscViewerDestroy()

This is most commonly used to view a sequential object that is part of a parallel object. For example PCView() on a PCBJACOBI could use this to obtain a PetscViewer that is used with the sequential KSP on one block of the preconditioner.

PetscViewerFlush() is run automatically at the beginning of PetscViewerGetSubViewer() and with PetscViewerRestoreSubViewer() for PETSCVIEWERASCII

PETSCVIEWERDRAW and PETSCVIEWERBINARY only support returning a singleton viewer on MPI rank 0, all other ranks will return a NULL viewer

Must be called by all MPI processes that share viewer, for processes that are not of interest you can pass PETSC_COMM_SELF.

For PETSCVIEWERASCII the viewers behavior is as follows:

There is currently incomplete error checking to ensure the user does not use the original viewer between the the calls to PetscViewerGetSubViewer() and PetscViewerRestoreSubViewer(). If the user does there could be errors in the viewing that go undetected or crash the code.

Complex use of this functionality with PETSCVIEWERASCII can result in output in unexpected order. This seems unavoidable.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscViewerFlush(), PetscViewerRestoreSubViewer()

src/sys/classes/viewer/interface/dupl.c

src/ts/tutorials/ex30.c src/vec/vec/tutorials/ex14f.F90 src/dm/tutorials/ex6.c src/vec/vec/tutorials/ex9f.F90

PetscViewerGetSubViewer_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerGetSubViewer_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerGetSubViewer_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerGetSubViewer_String() in src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerGetSubViewer(PetscViewer viewer, MPI_Comm comm, PetscViewer *outviewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerGetType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGetType/

**Contents:**
- PetscViewerGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the type of a PetscViewer.

viewer - the PetscViewer

type - PetscViewerType

type should not be retained for later use as it will be an invalid pointer if the PetscViewerType of viewer is changed.

Viewers: Looking at PETSc Objects, PetscViewerType, PetscViewer, PetscViewerCreate(), PetscViewerSetType(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/sys/classes/viewer/interface/view.c

src/dm/impls/plex/tutorials/ex19.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerGetType(PetscViewer viewer, PetscViewerType *type)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerType
```

---

## PetscViewerGLVisOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisOpen/

**Contents:**
- PetscViewerGLVisOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Opens a PETSCVIEWERGLVIS PetscViewer

Collective; No Fortran Support

comm - the MPI communicator

type - the viewer type: PETSC_VIEWER_GLVIS_SOCKET for real-time visualization or PETSC_VIEWER_GLVIS_DUMP for dumping to a file

name - either the hostname where the GLVis server is running or the base filename for dumping the data for subsequent visualizations

port - socket port where the GLVis server is listening. Not referenced when type is PETSC_VIEWER_GLVIS_DUMP

viewer - the PetscViewer object

-glvis_precision precision - Sets number of digits for floating point values

-glvis_size width,height - Sets the window size (in pixels)

-glvis_pause pause - Sets time (in seconds) that the program pauses after each visualization (0 is default, -1 implies every visualization)

-glvis_keys - Additional keys to configure visualization

-glvis_exec - Additional commands to configure visualization

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewerCreate(), PetscViewerSetType(), PetscViewerGLVisType

src/sys/classes/viewer/impls/glvis/glvis.c

src/ksp/ksp/tutorials/ex43.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERGLVIS
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscsys.h"    
PetscErrorCode PetscViewerGLVisOpen(MPI_Comm comm, PetscViewerGLVisType type, const char name[], PetscInt port, PetscViewer *viewer)
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_GLVIS_SOCKET
```

---

## PetscViewerGLVisSetFields#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetFields/

**Contents:**
- PetscViewerGLVisSetFields#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the required information to visualize different fields from a vector.

viewer - the PetscViewer of type PETSCVIEWERGLVIS

nf - number of fields to be visualized

fec_type - the type of finite element to be used to visualize the data (see FiniteElementCollection::Name() in MFEM)

dim - array of space dimension for field vectors (used to initialize the scene)

g2l - User routine to compute the local field vectors to be visualized; PetscObject is used in place of Vec on the prototype

Vfield - array of work vectors, one for each field

ctx - User context to store the relevant data to apply g2lfields

destroyctx - Destroy function for ctx

g2lfields is called on the vector V to be visualized in order to extract the relevant dofs to be put in Vfield, as

For vector spaces, the block size of Vfield[i] represents the vector dimension. The names of the Vfield vectors will be displayed in the window title.

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewerGLVisOpen(), PetscViewerCreate(), PetscViewerSetType(), PetscObjectSetName()

src/sys/classes/viewer/impls/glvis/glvis.c

src/ksp/ksp/tutorials/ex43.c

PetscViewerGLVisSetFields_GLVis(PetscViewer viewer, PetscInt nfields, const char *fec_type[], PetscInt dim[], PetscErrorCode (*g2l)() in src/sys/classes/viewer/impls/glvis/glvis.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscsys.h"    
PetscErrorCode PetscViewerGLVisSetFields(PetscViewer viewer, PetscInt nf, const char *fec_type[], PetscInt dim[], PetscErrorCode (*g2l)(PetscObject, PetscInt, PetscObject[], PetscCtx), PetscObject Vfield[], PetscCtx ctx, PetscCtxDestroyFn *destroyctx)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERGLVIS
```

Example 4 (unknown):
```unknown
g2lfields((PetscObject)V,nfields,(PetscObject*)Vfield[],ctx).
```

---

## PetscViewerGLVisSetPrecision#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetPrecision/

**Contents:**
- PetscViewerGLVisSetPrecision#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of digits for floating point values to be displayed

viewer - the PetscViewer of type PETSCVIEWERGLVIS

prec - the number of digits required

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewerGLVisOpen(), PetscViewerGLVisSetFields(), PetscViewerCreate(), PetscViewerSetType()

src/sys/classes/viewer/impls/glvis/glvis.c

PetscViewerGLVisSetPrecision_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscsys.h"    
PetscErrorCode PetscViewerGLVisSetPrecision(PetscViewer viewer, PetscInt prec)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERGLVIS
```

Example 4 (unknown):
```unknown
PETSCVIEWERGLVIS
```

---

## PetscViewerGLVisSetSnapId#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisSetSnapId/

**Contents:**
- PetscViewerGLVisSetSnapId#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the snapshot id. Only relevant when the PetscViewerGLVisType is PETSC_VIEWER_GLVIS_DUMP

viewer - the PetscViewer of type PETSCVIEWERGLVIS

id - the current snapshot id in a time-dependent simulation

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewerGLVisOpen(), PetscViewerGLVisSetFields(), PetscViewerCreate(), PetscViewerSetType()

src/sys/classes/viewer/impls/glvis/glvis.c

PetscViewerGLVisSetSnapId_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerGLVisType
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_GLVIS_DUMP
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscsys.h"    
PetscErrorCode PetscViewerGLVisSetSnapId(PetscViewer viewer, PetscInt id)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerGLVisType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerGLVisType/

**Contents:**
- PetscViewerGLVisType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

indicates what type of PETSCVIEWERGLVIS viewer to use

PETSC_VIEWER_GLVIS_DUMP - save the data to a file

PETSC_VIEWER_GLVIS_SOCKET - communicate the data to another program via a socket

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewerGLVisOpen()

include/petscviewer.h

src/ksp/ksp/tutorials/ex43.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERGLVIS
```

Example 2 (unknown):
```unknown
typedef enum {
  PETSC_VIEWER_GLVIS_DUMP,
  PETSC_VIEWER_GLVIS_SOCKET
} PetscViewerGLVisType;
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_GLVIS_DUMP
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_GLVIS_SOCKET
```

---

## PetscViewerHDF5GetBaseDimension2#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetBaseDimension2/

**Contents:**
- PetscViewerHDF5GetBaseDimension2#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Vectors of 1 dimension (i.e. bs/dof is 1) will be saved in the HDF5 file with a dimension of 2.

viewer - the PetscViewer, must be PETSCVIEWERHDF5

flg - if PETSC_TRUE the vector will always have at least a dimension of 2 even if that first dimension is of size 1

Setting this option allegedly makes code that reads the HDF5 in easier since they do not have a “special case” of a bs/dof of one when the dimension is lower. Others think the option is crazy.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetBaseDimension2_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetBaseDimension2(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5GetCollective#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetCollective/

**Contents:**
- PetscViewerHDF5GetCollective#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Return flag whether collective MPI-IO transfer mode is used for HDF5 reads and writes.

viewer - the PETSCVIEWERHDF5 PetscViewer

This setting works correctly only since HDF5 1.10.3 and if HDF5 was installed for MPI. For older versions, PETSC_FALSE will be always returned. For more details, see PetscViewerHDF5SetCollective().

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5SetCollective(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerHDF5Open()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetCollective_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetCollective(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewerHDF5GetCompress#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetCompress/

**Contents:**
- PetscViewerHDF5GetCompress#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the flag for compression

viewer - the PetscViewer of type PETSCVIEWERHDF5

flg - if PETSC_TRUE we will turn on compression

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5SetCompress()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetCompress_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetCompress(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5GetDefaultTimestepping#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetDefaultTimestepping/

**Contents:**
- PetscViewerHDF5GetDefaultTimestepping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the flag for default timestepping

viewer - the PetscViewer of type PETSCVIEWERHDF5

flg - if PETSC_TRUE we will assume that timestepping is on

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5SetDefaultTimestepping(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetDefaultTimestepping_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetDefaultTimestepping(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5GetFileId#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetFileId/

**Contents:**
- PetscViewerHDF5GetFileId#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieve the file id, this file ID then can be used in direct HDF5 calls

viewer - the PetscViewer

file_id - The file id

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open()

src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewerhdf5.h" 
PetscErrorCode PetscViewerHDF5GetFileId(PetscViewer viewer, hid_t *file_id)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5Open()
```

---

## PetscViewerHDF5GetGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetGroup/

**Contents:**
- PetscViewerHDF5GetGroup#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Get the current HDF5 group name (full path), set with PetscViewerHDF5PushGroup()/PetscViewerHDF5PopGroup().

viewer - the PetscViewer of type PETSCVIEWERHDF5

path - (Optional) The path relative to the pushed group

abspath - The absolute HDF5 path (group)

If path starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else path is relative to the current pushed group. NULL or empty path means the current pushed group.

The output abspath is newly allocated so needs to be freed.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5OpenGroup(), PetscViewerHDF5WriteGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetGroup_Internal() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerHDF5GetGroup_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerHDF5PushGroup()
```

Example 2 (unknown):
```unknown
PetscViewerHDF5PopGroup()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetGroup(PetscViewer viewer, const char path[], const char *abspath[])
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerHDF5GetSPOutput#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetSPOutput/

**Contents:**
- PetscViewerHDF5GetSPOutput#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Data is written to disk in single precision even if PETSc is compiled with double precision PetscReal.

viewer - the PetscViewer, must be of type PETSCVIEWERHDF5

flg - if PETSC_TRUE the data will be written to disk with single precision

Viewers: Looking at PETSc Objects, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen(), PetscReal, PetscViewerHDF5SetSPOutput()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetSPOutput_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetSPOutput(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PetscViewerFileSetMode()
```

Example 4 (unknown):
```unknown
PetscViewerCreate()
```

---

## PetscViewerHDF5GetTimestep#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5GetTimestep/

**Contents:**
- PetscViewerHDF5GetTimestep#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the current timestep for the HDF5 output. Fields are stacked in time.

viewer - the PetscViewer of type PETSCVIEWERHDF5

timestep - The timestep

This can be called only if the viewer is in the timestepping mode. See PetscViewerHDF5PushTimestepping() for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5IncrementTimestep(), PetscViewerHDF5SetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5GetTimestep_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5GetTimestep(PetscViewer viewer, PetscInt *timestep)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5HasAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasAttribute/

**Contents:**
- PetscViewerHDF5HasAttribute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Check whether an attribute exists

viewer - The PETSCVIEWERHDF5 viewer

parent - The parent dataset/group name

name - The attribute name

has - Flag for attribute existence

If parent starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else parent is relative to the current pushed group. NULL means the current pushed group.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5HasObjectAttribute(), PetscViewerHDF5WriteAttribute(), PetscViewerHDF5ReadAttribute(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5HasAttribute_Internal() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerHDF5HasAttribute_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5HasAttribute(PetscViewer viewer, const char parent[], const char name[], PetscBool *has)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5Open()
```

---

## PetscViewerHDF5HasDataset#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasDataset/

**Contents:**
- PetscViewerHDF5HasDataset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Check whether a given dataset exists in the HDF5 file

viewer - The PETSCVIEWERHDF5 viewer

path - The dataset path

has - Flag whether dataset exists

If path starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else path is relative to the current pushed group.

If path is NULL or empty, has is set to PETSC_FALSE.

If path exists but is not a dataset, has is set to PETSC_FALSE as well.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5HasObject(), PetscViewerHDF5HasAttribute(), PetscViewerHDF5HasGroup(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5HasDataset_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5HasDataset(PetscViewer viewer, const char path[], PetscBool *has)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewerHDF5HasGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasGroup/

**Contents:**
- PetscViewerHDF5HasGroup#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Check whether the current (pushed) group exists in the HDF5 file

viewer - The PETSCVIEWERHDF5 viewer

path - (Optional) The path relative to the pushed group

has - Flag for group existence

If path starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else path is relative to the current pushed group. NULL or empty path means the current pushed group.

If path exists but is not a group, PETSC_FALSE is returned.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5HasAttribute(), PetscViewerHDF5HasDataset(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup(), PetscViewerHDF5OpenGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5HasGroup_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5HasGroup(PetscViewer viewer, const char path[], PetscBool *has)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5HasObjectAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasObjectAttribute/

**Contents:**
- PetscViewerHDF5HasObjectAttribute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Check whether an attribute is attached to the dataset matching the given PetscObject by name

viewer - The PETSCVIEWERHDF5 viewer

obj - The object whose name is used to lookup the parent dataset, relative to the current group.

name - The attribute name

has - Flag for attribute existence

This fails if current_group/object_name doesn’t resolve to a dataset (the path doesn’t exist or is not a dataset). You might want to check first if it does using PetscViewerHDF5HasObject().

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5HasAttribute(), PetscViewerHDF5WriteObjectAttribute(), PetscViewerHDF5ReadObjectAttribute(), PetscViewerHDF5HasObject(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscObject
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5HasObjectAttribute(PetscViewer viewer, PetscObject obj, const char name[], PetscBool *has)
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5HasObject()
```

---

## PetscViewerHDF5HasObject#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5HasObject/

**Contents:**
- PetscViewerHDF5HasObject#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Check whether a dataset with the same name as given object exists in the HDF5 file under current group

viewer - The PETSCVIEWERHDF5 viewer

obj - The named object

has - Flag for dataset existence

If the object is unnamed, an error occurs.

If the path current_group/object_name exists but is not a dataset, has is set to PETSC_FALSE as well.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5HasDataset(), PetscViewerHDF5HasAttribute(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/ksp/ksp/tutorials/ex27.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5HasObject(PetscViewer viewer, PetscObject obj, PetscBool *has)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5IncrementTimestep#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5IncrementTimestep/

**Contents:**
- PetscViewerHDF5IncrementTimestep#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Increments current timestep for the HDF5 output. Fields are stacked in time.

viewer - the PetscViewer of type PETSCVIEWERHDF5

This can be called only if the viewer is in timestepping mode. See PetscViewerHDF5PushTimestepping() for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5SetTimestep(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/vec/vec/tutorials/ex19.c

PetscViewerHDF5IncrementTimestep_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5IncrementTimestep(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5IsTimestepping#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5IsTimestepping/

**Contents:**
- PetscViewerHDF5IsTimestepping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Ask the viewer whether it is in timestepping mode currently.

viewer - the PetscViewer of type PETSCVIEWERHDF5

flg - is timestepping active?

See PetscViewerHDF5PushTimestepping() for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5PopTimestepping(), PetscViewerHDF5SetTimestep(), PetscViewerHDF5IncrementTimestep(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5IsTimestepping_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5IsTimestepping(PetscViewer viewer, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5Load#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5Load/

**Contents:**
- PetscViewerHDF5Load#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Read a raw array from the PETSCVIEWERHDF5 dataset in parallel

Collective; No Fortran Support

viewer - The PETSCVIEWERHDF5 viewer

name - The dataset name

datatype - The HDF5 datatype of the items in the dataset

map - The layout which specifies array partitioning, on output the set up layout (with global size and blocksize according to dataset)

newarr - The partitioned array, a memory image of the given dataset

This is intended mainly for internal use; users should use higher level routines such as ISLoad(), VecLoad(), DMLoad().

The array is partitioned according to the given PetscLayout which is converted to an HDF5 hyperslab.

This name is relative to the current group returned by PetscViewerHDF5OpenGroup().

PetscViewer, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushGroup(), PetscViewerHDF5OpenGroup(), PetscViewerHDF5ReadSizes(), VecLoad(), ISLoad(), PetscLayout

src/vec/is/utils/hdf5/hdf5io.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 2 (unknown):
```unknown
#include "petsclayoutdf5.h"   
#include "petscis.h"   
PetscErrorCode PetscViewerHDF5Load(PetscViewer viewer, const char name[], PetscLayout map, hid_t datatype, void **newarr)
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## PetscViewerHDF5OpenGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5OpenGroup/

**Contents:**
- PetscViewerHDF5OpenGroup#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Open the HDF5 group with the name (full path) returned by PetscViewerHDF5GetGroup(), and return this group’s ID and file ID. If PetscViewerHDF5GetGroup() yields NULL, then group ID is file ID.

viewer - the PetscViewer of type PETSCVIEWERHDF5

path - (Optional) The path relative to the pushed group

fileId - The HDF5 file ID

groupId - The HDF5 group ID

If path starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else path is relative to the current pushed group. NULL or empty path means the current pushed group.

If the viewer is writable, the group is created if it doesn’t exist yet.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup(), PetscViewerHDF5WriteGroup()

src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerHDF5GetGroup()
```

Example 2 (unknown):
```unknown
PetscViewerHDF5GetGroup()
```

Example 3 (unknown):
```unknown
#include "petscviewerhdf5.h" 
PetscErrorCode PetscViewerHDF5OpenGroup(PetscViewer viewer, const char path[], hid_t *fileId, hid_t *groupId)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerHDF5Open#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5Open/

**Contents:**
- PetscViewerHDF5Open#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Opens a file for HDF5 input/output as a PETSCVIEWERHDF5 PetscViewer

comm - MPI communicator

hdf5v - PetscViewer for HDF5 input/output to use with the specified file

-viewer_hdf5_base_dimension2 - turns on (true) or off (false) using a dimension of 2 in the HDF5 file even if the bs/dof of the vector is 1

-viewer_hdf5_sp_output - forces (if true) the viewer to write data in single precision independent on the precision of PetscReal

Reading is always available, regardless of the mode. Available modes are

In case of FILE_MODE_APPEND / FILE_MODE_UPDATE, any stored object (dataset, attribute) can be selectively overwritten if the same fully qualified name (/group/path/to/object) is specified.

This PetscViewer should be destroyed with PetscViewerDestroy().

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), PetscViewerHDF5SetBaseDimension2(), PetscViewerHDF5SetSPOutput(), PetscViewerHDF5GetBaseDimension2(), VecView(), MatView(), VecLoad(), MatLoad(), PetscFileMode, PetscViewer, PetscViewerSetType(), PetscViewerFileSetMode(), PetscViewerFileSetName()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/vec/vec/tutorials/ex10.c src/ts/tutorials/ex30.c src/dm/tutorials/ex10.c src/dm/tutorials/ex9.c src/tao/tutorials/ex3.c src/dm/impls/plex/tutorials/ex5.c src/vec/vec/tutorials/ex19.c src/ksp/ksp/tutorials/ex27.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5Open(MPI_Comm comm, const char name[], PetscFileMode type, PetscViewer *hdf5v)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerHDF5PathIsRelative#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PathIsRelative/

**Contents:**
- PetscViewerHDF5PathIsRelative#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether an HDF5 path string is relative (does not begin with /).

emptyIsRelative - the value to return when path is empty

rel - PETSC_TRUE if path is relative, PETSC_FALSE if it is absolute

PetscViewer, PETSCVIEWERHDF5, PetscViewerHDF5PushGroup(), PetscViewerHDF5GetGroup()

include/petscviewerhdf5.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
static inline PetscErrorCode PetscViewerHDF5PathIsRelative(const char path[], PetscBool emptyIsRelative, PetscBool *rel)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5PopGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PopGroup/

**Contents:**
- PetscViewerHDF5PopGroup#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Return the current HDF5 group for output to the previous value

viewer - the PetscViewer of type PETSCVIEWERHDF5

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushGroup(), PetscViewerHDF5GetGroup(), PetscViewerHDF5OpenGroup(), PetscViewerHDF5WriteGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/ts/tutorials/ex30.c src/vec/vec/tutorials/ex19.c src/snes/tutorials/ex12.c

PetscViewerHDF5PopGroup_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5PopGroup(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5PopTimestepping#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PopTimestepping/

**Contents:**
- PetscViewerHDF5PopTimestepping#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Deactivate timestepping mode for subsequent HDF5 reading and writing.

viewer - the PetscViewer of type PETSCVIEWERHDF5

See PetscViewerHDF5PushTimestepping() for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5IsTimestepping(), PetscViewerHDF5SetTimestep(), PetscViewerHDF5IncrementTimestep(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/vec/vec/tutorials/ex19.c

PetscViewerHDF5PopTimestepping_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5PopTimestepping(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5PushGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PushGroup/

**Contents:**
- PetscViewerHDF5PushGroup#
- Synopsis#
- Input Parameters#
- Notes#
- Example#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the current HDF5 group for output

viewer - the PetscViewer of type PETSCVIEWERHDF5

name - The group name

This is designed to mnemonically resemble the Unix cd command.

Suppose the current group is “/a”.

The root group “/” is internally stored as NULL.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup(), PetscViewerHDF5OpenGroup(), PetscViewerHDF5WriteGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/ts/tutorials/ex30.c src/vec/vec/tutorials/ex19.c src/snes/tutorials/ex12.c src/tao/tutorials/ex3.c

PetscViewerHDF5PushGroup_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5PushGroup(PetscViewer viewer, const char name[])
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (typescript):
```typescript
If name begins with '/', it is interpreted as an absolute path fully replacing current group, otherwise it is taken as relative to the current group.
  `NULL`, empty string, or any sequence of all slashes (e.g. "///") is interpreted as the root group "/".
  "." means the current group is pushed again.
```

---

## PetscViewerHDF5PushTimestepping#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5PushTimestepping/

**Contents:**
- PetscViewerHDF5PushTimestepping#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Activate timestepping mode for subsequent HDF5 reading and writing.

viewer - the PetscViewer of type PETSCVIEWERHDF5

On first PetscViewerHDF5PushTimestepping(), the initial time step is set to 0. Next timesteps can then be set using PetscViewerHDF5IncrementTimestep() or PetscViewerHDF5SetTimestep(). Current timestep value determines which timestep is read from or written to any dataset on the next HDF5 I/O operation [e.g. VecView()]. Use PetscViewerHDF5PopTimestepping() to deactivate timestepping mode; calling it by the end of the program is NOT mandatory. Current timestep is remembered between PetscViewerHDF5PopTimestepping() and the next PetscViewerHDF5PushTimestepping().

If a dataset was stored with timestepping, it can be loaded only in the timestepping mode again. Loading a timestepped dataset with timestepping disabled, or vice-versa results in an error.

Timestepped HDF5 dataset has an extra dimension and attribute “timestepping” set to true.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PopTimestepping(), PetscViewerHDF5IsTimestepping(), PetscViewerHDF5SetTimestep(), PetscViewerHDF5IncrementTimestep(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/vec/vec/tutorials/ex19.c

PetscViewerHDF5PushTimestepping_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5PushTimestepping(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5ReadAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5ReadAttribute/

**Contents:**
- PetscViewerHDF5ReadAttribute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

viewer - The PETSCVIEWERHDF5 viewer

parent - The parent dataset/group name

name - The attribute name

datatype - The attribute type

defaultValue - The pointer to the default value

value - The pointer to the read HDF5 attribute value

If defaultValue is NULL and the attribute is not found, an error occurs.

If defaultValue is not NULL and the attribute is not found, defaultValue is copied to value.

The pointers defaultValue and value can be the same; for instance

is valid, but make sure the default value is initialized.

If the datatype is PETSC_STRING, the output string is newly allocated so one must PetscFree() it when no longer needed.

If parent starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else parent is relative to the current pushed group. NULL means the current pushed group.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5ReadObjectAttribute(), PetscViewerHDF5WriteAttribute(), PetscViewerHDF5HasAttribute(), PetscViewerHDF5HasObject(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/ts/tutorials/ex30.c

PetscViewerHDF5ReadAttribute_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5ReadAttribute(PetscViewer viewer, const char parent[], const char name[], PetscDataType datatype, const void *defaultValue, void *value)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
defaultValue
```

Example 4 (unknown):
```unknown
defaultValue
```

---

## PetscViewerHDF5ReadObjectAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5ReadObjectAttribute/

**Contents:**
- PetscViewerHDF5ReadObjectAttribute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Read an attribute from the dataset matching the given PetscObject by name

viewer - The PETSCVIEWERHDF5 viewer

obj - The object whose name is used to lookup the parent dataset, relative to the current group.

name - The attribute name

datatype - The attribute type

defaultValue - The default attribute value

value - The attribute value

This fails if current_group/object_name doesn’t resolve to a dataset (the path doesn’t exist or is not a dataset). You might want to check first if it does using PetscViewerHDF5HasObject().

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5ReadAttribute(), PetscViewerHDF5WriteObjectAttribute(), PetscViewerHDF5HasObjectAttribute(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscObject
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5ReadObjectAttribute(PetscViewer viewer, PetscObject obj, const char name[], PetscDataType datatype, void *defaultValue, void *value)
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5HasObject()
```

---

## PetscViewerHDF5ReadSizes#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5ReadSizes/

**Contents:**
- PetscViewerHDF5ReadSizes#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- timesteps (optional), 2) # blocks, 3) # elements per block (optional), 4) real and imaginary part (only for complex).
- See Also#
- Level#
- Location#

Read block size and global size of a Vec or IS stored in an HDF5 file.

viewer - The PETSCVIEWERHDF5 viewer

name - The dataset name

The dataset is stored as an HDF5 dataspace with 1-4 dimensions in the order

The dataset can be stored as a 2D dataspace even if its blocksize is 1; see PetscViewerHDF5SetBaseDimension2().

PetscViewer, PETSCVIEWERHDF5, PetscViewerHDF5Open(), VecLoad(), ISLoad(), VecGetSize(), ISGetSize(), PetscViewerHDF5SetBaseDimension2()

src/vec/is/utils/hdf5/hdf5io.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsclayoutdf5.h"   
#include "petscis.h"   
PetscErrorCode PetscViewerHDF5ReadSizes(PetscViewer viewer, const char name[], PetscInt *bs, PetscInt *N)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PetscViewerHDF5SetBaseDimension2()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerHDF5SetBaseDimension2#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetBaseDimension2/

**Contents:**
- PetscViewerHDF5SetBaseDimension2#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Vectors of 1 dimension (i.e. bs/dof is 1) will be saved in the HDF5 file with a dimension of 2.

viewer - the PetscViewer; if it is a PETSCVIEWERHDF5 then this command is ignored

flg - if PETSC_TRUE the vector will always have at least a dimension of 2 even if that first dimension is of size 1

-viewer_hdf5_base_dimension2 - turns on (true) or off (false) using a dimension of 2 in the HDF5 file even if the bs/dof of the vector is 1

Setting this option allegedly makes code that reads the HDF5 in easier since they do not have a “special case” of a bs/dof of one when the dimension is lower. Others think the option is crazy.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/dm/tutorials/ex9.c

PetscViewerHDF5SetBaseDimension2_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetBaseDimension2(PetscViewer viewer, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5SetCollective#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetCollective/

**Contents:**
- PetscViewerHDF5SetCollective#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Implementations#

Use collective MPI-IO transfer mode for HDF5 reads and writes.

Logically Collective; flg must contain common value

viewer - the PetscViewer; if it is not PETSCVIEWERHDF5 then this command is ignored

flg - PETSC_TRUE for collective mode; PETSC_FALSE for independent mode (default)

-viewer_hdf5_collective - turns on (true) or off (false) collective transfers

Collective mode gives the MPI-IO layer underneath HDF5 a chance to do some additional collective optimizations and hence can perform better. However, this works correctly only since HDF5 1.10.3 and if HDF5 is installed for MPI; hence, we ignore this setting for older versions.

In the HDF5 layer, PETSC_TRUE / PETSC_FALSE means H5Pset_dxpl_mpio() is called with H5FD_MPIO_COLLECTIVE / H5FD_MPIO_INDEPENDENT, respectively. This in turn means use of MPI_File_{read,write}all / MPI_File{read,write} in the MPI-IO layer, respectively. See HDF5 documentation and MPI-IO documentation for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5GetCollective(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerHDF5Open()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5SetCollective_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetCollective(PetscViewer viewer, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewerHDF5SetCompress#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetCompress/

**Contents:**
- PetscViewerHDF5SetCompress#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the flag for compression

viewer - the PetscViewer; if it is not PETSCVIEWERHDF5 then this command is ignored

flg - if PETSC_TRUE we will turn on compression

-viewer_hdf5_compress - turns on (true) or off (false) compression

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5GetCompress()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5SetCompress_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetCompress(PetscViewer viewer, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5SetDefaultTimestepping#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetDefaultTimestepping/

**Contents:**
- PetscViewerHDF5SetDefaultTimestepping#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the flag for default timestepping

viewer - the PetscViewer; if it is not PETSCVIEWERHDF5 then this command is ignored

flg - if PETSC_TRUE we will assume that timestepping is on

-viewer_hdf5_default_timestepping - turns on (true) or off (false) default timestepping

If the timestepping attribute is not found for an object, then the default timestepping is used

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5GetDefaultTimestepping(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5SetDefaultTimestepping_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetDefaultTimestepping(PetscViewer viewer, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5SetSPOutput#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetSPOutput/

**Contents:**
- PetscViewerHDF5SetSPOutput#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Data is written to disk in single precision even if PETSc is compiled with double precision PetscReal.

viewer - the PetscViewer; if it is a PETSCVIEWERHDF5 then this command is ignored

flg - if PETSC_TRUE the data will be written to disk with single precision

-viewer_hdf5_sp_output - turns on (true) or off (false) output in single precision

Setting this option does not make any difference if PETSc is compiled with single precision in the first place. It does not affect reading datasets (HDF5 handle this internally).

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerFileSetMode(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerBinaryOpen(), PetscReal, PetscViewerHDF5GetSPOutput()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5SetSPOutput_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetSPOutput(PetscViewer viewer, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerFileSetMode()
```

---

## PetscViewerHDF5SetTimestep#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5SetTimestep/

**Contents:**
- PetscViewerHDF5SetTimestep#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the current timestep for the HDF5 output. Fields are stacked in time.

viewer - the PetscViewer of type PETSCVIEWERHDF5

timestep - The timestep

This can be called only if the viewer is in timestepping mode. See PetscViewerHDF5PushTimestepping() for details.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushTimestepping(), PetscViewerHDF5IncrementTimestep(), PetscViewerHDF5GetTimestep()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/vec/vec/tutorials/ex19.c

PetscViewerHDF5SetTimestep_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5SetTimestep(PetscViewer viewer, PetscInt timestep)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5PushTimestepping()
```

---

## PetscViewerHDF5WriteAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteAttribute/

**Contents:**
- PetscViewerHDF5WriteAttribute#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

viewer - The PETSCVIEWERHDF5 viewer

parent - The parent dataset/group name

name - The attribute name

datatype - The attribute type

value - The attribute value

If parent starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else parent is relative to the current pushed group. NULL means the current pushed group.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5WriteObjectAttribute(), PetscViewerHDF5ReadAttribute(), PetscViewerHDF5HasAttribute(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

src/ts/tutorials/ex30.c

PetscViewerHDF5WriteAttribute_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5WriteAttribute(PetscViewer viewer, const char parent[], const char name[], PetscDataType datatype, const void *value)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5Open()
```

---

## PetscViewerHDF5WriteGroup#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteGroup/

**Contents:**
- PetscViewerHDF5WriteGroup#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Ensure the HDF5 group exists in the HDF5 file

viewer - the PetscViewer of type PETSCVIEWERHDF5

path - (Optional) The path relative to the pushed group

If path starts with ‘/’, it is taken as an absolute path overriding currently pushed group, else path is relative to the current pushed group. NULL or empty path means the current pushed group.

This will fail if the viewer is not writable.

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup(), PetscViewerHDF5OpenGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

PetscViewerHDF5WriteGroup_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5WriteGroup(PetscViewer viewer, const char path[])
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PetscViewerHDF5WriteObjectAttribute#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerHDF5WriteObjectAttribute/

**Contents:**
- PetscViewerHDF5WriteObjectAttribute#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Write an attribute to the dataset matching the given PetscObject by name

viewer - The PETSCVIEWERHDF5 viewer

obj - The object whose name is used to lookup the parent dataset, relative to the current group.

name - The attribute name

datatype - The attribute type

value - The attribute value

This fails if the path current_group/object_name doesn’t resolve to a dataset (the path doesn’t exist or is not a dataset). You might want to check first if it does using PetscViewerHDF5HasObject().

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerHDF5WriteAttribute(), PetscViewerHDF5ReadObjectAttribute(), PetscViewerHDF5HasObjectAttribute(), PetscViewerHDF5HasObject(), PetscViewerHDF5PushGroup(), PetscViewerHDF5PopGroup(), PetscViewerHDF5GetGroup()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscObject
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerHDF5WriteObjectAttribute(PetscViewer viewer, PetscObject obj, const char name[], PetscDataType datatype, const void *value)
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5HasObject()
```

---

## PETSCVIEWERHDF5#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERHDF5/

**Contents:**
- PETSCVIEWERHDF5#
- See Also#
- Level#
- Location#
- Examples#

A viewer that writes to an HDF5 file

Viewers: Looking at PETSc Objects, PetscViewerHDF5Open(), PetscViewerStringSPrintf(), PetscViewerSocketOpen(), PetscViewerDrawOpen(), PETSCVIEWERSOCKET, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PETSCVIEWERDRAW, PETSCVIEWERSTRING, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

src/snes/tutorials/ex12.c src/ksp/ksp/tutorials/ex27.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerHDF5Open()
```

Example 2 (unknown):
```unknown
PetscViewerStringSPrintf()
```

Example 3 (unknown):
```unknown
PetscViewerSocketOpen()
```

Example 4 (unknown):
```unknown
PetscViewerDrawOpen()
```

---

## PetscViewerInitializePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerInitializePackage/

**Contents:**
- PetscViewerInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscViewer package.

Viewers: Looking at PETSc Objects, PetscViewer, PetscInitialize(), PetscViewerFinalizePackage()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscViewerMathematicaClearName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaClearName/

**Contents:**
- PetscViewerMathematicaClearName#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Use the default name for objects communicated to Mathematica

viewer - The Mathematica viewer

PETSCVIEWERMATHEMATICA, PetscViewerMathematicaGetName(), PetscViewerMathematicaSetName()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaClearName(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 3 (unknown):
```unknown
PetscViewerMathematicaGetName()
```

Example 4 (unknown):
```unknown
PetscViewerMathematicaSetName()
```

---

## PetscViewerMathematicaFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaFinalizePackage/

**Contents:**
- PetscViewerMathematicaFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc interface to Mathematica. It is called from PetscFinalize().

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaFinalizePackage(void)
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

---

## PetscViewerMathematicaGetName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaGetName/

**Contents:**
- PetscViewerMathematicaGetName#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieve the default name for objects communicated to Mathematica via PETSCVIEWERMATHEMATICA

viewer - The Mathematica viewer

name - The name for new objects created in Mathematica

PETSCVIEWERMATHEMATICA, PetscViewerMathematicaSetName(), PetscViewerMathematicaClearName()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaGetName(PetscViewer viewer, const char **name)
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 4 (unknown):
```unknown
PetscViewerMathematicaSetName()
```

---

## PetscViewerMathematicaInitializePackage#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaInitializePackage/

**Contents:**
- PetscViewerMathematicaInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PETSc interface to Mathematica. It is called from PetscViewerInitializePackage().

PetscSysInitializePackage(), PetscInitialize()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerInitializePackage()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscSysInitializePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscViewerMathematicaOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaOpen/

**Contents:**
- PetscViewerMathematicaOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Communicates with Mathemtica using MathLink.

comm - The MPI communicator

port - [optional] The port to connect on, or PETSC_DECIDE

machine - [optional] The machine to run Mathematica on, or NULL

mode - [optional] The connection mode, or NULL

v - The Mathematica viewer

-viewer_math_linkhost machine - The host machine for the kernel

-viewer_math_linkname name - The full link name for the connection

-viewer_math_linkport port - The port for the connection

-viewer_math_mode mode - The mode, e.g. Launch, Connect

-viewer_math_type type - The plot type, e.g. Triangulation, Vector

-viewer_math_graphics output - The output type, e.g. Motif, PS, PSFile

Most users should employ the following commands to access the Mathematica viewers

PETSCVIEWERMATHEMATICA, MatView(), VecView()

src/sys/classes/viewer/impls/mathematica/mathematica.c

src/vec/vec/tutorials/ex15.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaOpen(MPI_Comm comm, int port, const char machine[], const char mode[], PetscViewer *v)
```

Example 2 (unknown):
```unknown
PetscViewerMathematicaOpen(MPI_Comm comm, int port, char *machine, char *mode, PetscViewer &viewer)
    MatView(Mat matrix, PetscViewer viewer)

                or

    PetscViewerMathematicaOpen(MPI_Comm comm, int port, char *machine, char *mode, PetscViewer &viewer)
    VecView(Vec vector, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

---

## PetscViewerMathematicaPutCSRMatrix#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaPutCSRMatrix/

**Contents:**
- PetscViewerMathematicaPutCSRMatrix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Send a sparse matrix in CSR format to a Mathematica kernel as a LinearAlgebraCSRMatrix bound to a symbol in the kernel’s namespace.

viewer - the PETSCVIEWERMATHEMATICA viewer

m - the number of rows

n - the number of columns

i - CSR row pointers of length m + 1

j - CSR column indices

a - CSR nonzero values

The Mathematica symbol name defaults to mat and can be changed with PetscViewerMathematicaSetName().

PetscViewer, PETSCVIEWERMATHEMATICA, PetscViewerMathematicaPutMatrix(), PetscViewerMathematicaSetName()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaPutCSRMatrix(PetscViewer viewer, int m, int n, int *i, int *j, PetscReal *a)
```

Example 2 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 3 (unknown):
```unknown
PetscViewerMathematicaSetName()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerMathematicaPutMatrix#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaPutMatrix/

**Contents:**
- PetscViewerMathematicaPutMatrix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Send a dense matrix to a Mathematica kernel as a two-dimensional array bound to a symbol in the kernel’s namespace.

viewer - the PETSCVIEWERMATHEMATICA viewer

m - the number of rows

n - the number of columns

a - the matrix values, in column-major order, of length m * n

The Mathematica symbol name defaults to mat and can be changed with PetscViewerMathematicaSetName().

PetscViewer, PETSCVIEWERMATHEMATICA, PetscViewerMathematicaPutCSRMatrix(), PetscViewerMathematicaSetName()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaPutMatrix(PetscViewer viewer, int m, int n, PetscReal *a)
```

Example 2 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 3 (unknown):
```unknown
PetscViewerMathematicaSetName()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerMathematicaSetName#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaSetName/

**Contents:**
- PetscViewerMathematicaSetName#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Override the default name for objects communicated to Mathematica via PETSCVIEWERMATHEMATICA

viewer - The Mathematica viewer

name - The name for new objects created in Mathematica

PETSCVIEWERMATHEMATICA, PetscViewerMathematicaClearName()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaSetName(PetscViewer viewer, const char name[])
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATHEMATICA
```

Example 4 (unknown):
```unknown
PetscViewerMathematicaClearName()
```

---

## PetscViewerMathematicaSkipPackets#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMathematicaSkipPackets/

**Contents:**
- PetscViewerMathematicaSkipPackets#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Discard packets sent by Mathematica until a certain packet type is received

viewer - The Mathematica viewer

type - The packet type to search for, e.g RETURNPKT

PetscViewerMathematicaSetName(), PetscViewerMathematicaGetVector()

src/sys/classes/viewer/impls/mathematica/mathematica.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscViewerMathematicaSkipPackets(PetscViewer viewer, int type)
```

Example 2 (unknown):
```unknown
PetscViewerMathematicaSetName()
```

Example 3 (unknown):
```unknown
PetscViewerMathematicaGetVector()
```

---

## PetscViewerMatlabGetArray#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabGetArray/

**Contents:**
- PetscViewerMatlabGetArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets a variable from a PETSCVIEWERMATLAB viewer into an array

Not Collective; only processor zero reads in the array

mfile - the MATLAB file viewer

m - the first dimensions of array

n - the second dimensions of array

array - the array (represented in one dimension), must of be length m * n

name - the MATLAB name of array

Only reads in array values on processor 0.

PETSCVIEWERMATLAB, PetscViewerMatlabPutArray()

src/sys/classes/viewer/impls/matlab/vmatlab.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
#include "petscmat.h"      
PetscErrorCode PetscViewerMatlabGetArray(PetscViewer mfile, int m, int n, PetscScalar array[], const char *name)
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 4 (unknown):
```unknown
PetscViewerMatlabPutArray()
```

---

## PetscViewerMatlabOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabOpen/

**Contents:**
- PetscViewerMatlabOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Opens a MATLAB .mat file for output

comm - MPI communicator

binv - PetscViewer for MATLAB output to use with the specified file

This PetscViewer should be destroyed with PetscViewerDestroy().

For writing files it only opens the file on processor 0 in the communicator.

This only saves Vecs it cannot be used to save Mats. We recommend using the PETSCVIEWERBINARY to save objects to be loaded into MATLAB instead of this routine.

PETSc must be configured with the option --with-matlab for this functionality

PETSCVIEWERMATLAB, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), PETSCVIEWERBINARY, PetscViewerBinaryOpen(), VecView(), MatView(), VecLoad(), MatLoad()

src/sys/classes/viewer/impls/matlab/vmatlab.c

src/dm/tutorials/ex1.c src/snes/tutorials/ex30.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"   
#include "petscmat.h"      
PetscErrorCode PetscViewerMatlabOpen(MPI_Comm comm, const char name[], PetscFileMode type, PetscViewer *binv)
```

Example 2 (bash):
```bash
FILE_MODE_WRITE - create new file for MATLAB output
    FILE_MODE_READ - open existing file for MATLAB input
    FILE_MODE_WRITE - open existing file for MATLAB output
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerDestroy()
```

---

## PetscViewerMatlabPutArray#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabPutArray/

**Contents:**
- PetscViewerMatlabPutArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Puts an array into the PETSCVIEWERMATLAB viewer.

Not Collective, only processor zero saves array

m - the first dimensions of array

n - the second dimensions of array

array - the array (represented in one dimension)

name - the MATLAB name of array

Only writes array values on processor 0.

PETSCVIEWERMATLAB, PetscViewerMatlabGetArray()

src/sys/classes/viewer/impls/matlab/vmatlab.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
#include "petscmat.h"      
PetscErrorCode PetscViewerMatlabPutArray(PetscViewer mfile, int m, int n, const PetscScalar *array, const char *name)
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 4 (unknown):
```unknown
PetscViewerMatlabGetArray()
```

---

## PetscViewerMatlabPutVariable#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMatlabPutVariable/

**Contents:**
- PetscViewerMatlabPutVariable#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Write a raw MATLAB mxArray variable into a PETSCVIEWERMATLAB file under a chosen name.

Not Collective; only processor zero writes the variable

viewer - the PETSCVIEWERMATLAB viewer

name - the MATLAB variable name

mat - the mxArray * variable to write (cast to void *)

PetscViewer, PETSCVIEWERMATLAB, PetscViewerMatlabPutArray(), PetscViewerMatlabGetArray(), PetscViewerMatlabOpen()

src/sys/classes/viewer/impls/matlab/vmatlab.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 2 (unknown):
```unknown
#include "petscviewer.h"   
#include "petscmat.h"      
PetscErrorCode PetscViewerMatlabPutVariable(PetscViewer viewer, const char *name, void *mat)
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSCVIEWERMATLAB#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERMATLAB/

**Contents:**
- PETSCVIEWERMATLAB#
- Notes#
- See Also#
- Level#
- Location#

A viewer that saves the variables into a MATLAB .mat file that may be read into MATLAB with load(‘filename’).

Currently can only save PETSc vectors to .mat files, not matrices (use the PETSCVIEWERBINARY and ${PETSC_DIR}/share/petsc/matlab/PetscBinaryRead.m to read matrices into MATLAB).

For parallel vectors obtained with DMCreateGlobalVector() or DMGetGlobalVector() the vectors are saved to the .mat file in natural ordering. You can use DMView() to save the DMDA information to the .mat file the fields in the MATLAB loaded da variable give the array dimensions so you can reshape the MATLAB vector to the same multidimensional shape as it had in PETSc for plotting etc. For example,

In your PETSc C/C++ code (assuming a two dimensional DMDA with one degree of freedom per node)

If you wish to put the same variable into the .mat file several times you need to give it a new name before each call to view.

Use PetscViewerMatlabPutArray() to just put an array of doubles into the .mat file

PETSC_VIEWER_MATLAB_(), PETSC_VIEWER_MATLAB_SELF, PETSC_VIEWER_MATLAB_WORLD, PetscViewerCreate(), PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERBINARY, PETSCVIEWERASCII, PETSCVIEWERDRAW, PETSC_VIEWER_STDOUT_(), PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscMatlabEngine

src/sys/classes/viewer/impls/matlab/vmatlab.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMGetGlobalVector()
```

Example 4 (unknown):
```unknown
PetscObjectSetName((PetscObject)x,"x");
                VecView(x,PETSC_VIEWER_MATLAB_WORLD);
                PetscObjectSetName((PetscObject)da,"da");
                DMView(x,PETSC_VIEWER_MATLAB_WORLD);
```

---

## PetscViewerMonitorLGSetUp#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerMonitorLGSetUp/

**Contents:**
- PetscViewerMonitorLGSetUp#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

sets up a viewer to be used by line graph monitoring routines such as KSPMonitorResidualDrawLG()

viewer - the viewer in which to display the line graphs, it not a PETSCVIEWERDRAW it will set to that PetscViewerType

host - the host to open the window on, NULL indicates the local host

title - the title at the top of the window

metric - the label above the graph

l - the number of curves

names - the names of each curve to be used in displaying the legend. May be NULL

x - horizontal screen coordinate of the upper left corner of window, or use PETSC_DECIDE

y - vertical screen coordinate of the upper left corner of window, or use PETSC_DECIDE

m - window width in pixels, or may use PETSC_DECIDE or PETSC_DRAW_FULL_SIZE, PETSC_DRAW_HALF_SIZE,PETSC_DRAW_THIRD_SIZE, PETSC_DRAW_QUARTER_SIZE

n - window height in pixels, or may use PETSC_DECIDE or PETSC_DRAW_FULL_SIZE, PETSC_DRAW_HALF_SIZE,PETSC_DRAW_THIRD_SIZE, PETSC_DRAW_QUARTER_SIZE

PetscViewer(), PETSCVIEWERDRAW, PetscViewerDrawGetDrawLG(), PetscViewerDrawOpen(), PetscViewerDrawSetInfo()

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
KSPMonitorResidualDrawLG()
```

Example 2 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscErrorCode PetscViewerMonitorLGSetUp(PetscViewer viewer, const char host[], const char title[], const char metric[], PetscInt l, const char *names[], int x, int y, int m, int n) PeNS
```

Example 3 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 4 (unknown):
```unknown
PetscViewerType
```

---

## PetscViewerPopFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPopFormat/

**Contents:**
- PetscViewerPopFormat#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Resets the format for a PetscViewer to the value it had before the previous call to PetscViewerPushFormat()

viewer - the PetscViewer

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerFormat, PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), MatView(), VecView(), PetscViewerSetFormat(), PetscViewerPushFormat()

src/sys/classes/viewer/interface/viewa.c

src/ksp/ksp/tutorials/ex55.c src/ksp/ksp/tutorials/ex56.c src/vec/vec/tutorials/ex3.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ksp/ksp/tutorials/ex54.c src/vec/is/sf/tutorials/ex1.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c src/ksp/ksp/tutorials/ex76.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerPushFormat()
```

Example 3 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscViewerPopFormat(PetscViewer viewer)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerPushFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPushFormat/

**Contents:**
- PetscViewerPushFormat#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the format for a PetscViewer.

viewer - the PetscViewer

See PetscViewerFormat for available values

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerFormat, PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), MatView(), VecView(), PetscViewerSetFormat(), PetscViewerPopFormat()

src/sys/classes/viewer/interface/viewa.c

src/ksp/ksp/tutorials/ex55.c src/ksp/ksp/tutorials/ex2f.F90 src/snes/tutorials/ex1f.F90 src/mat/tutorials/ex10.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ksp/ksp/tutorials/ex54.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c src/ksp/ksp/tutorials/ex76.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscViewerPushFormat(PetscViewer viewer, PetscViewerFormat format)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerFormat
```

---

## PetscViewerPythonCreate#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPythonCreate/

**Contents:**
- PetscViewerPythonCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a PetscViewer object implemented in Python.

comm - MPI communicator

pyname - full dotted Python name [package].module[.{class|function}]

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerType, PETSCVIEWERPYTHON, PetscViewerPythonSetType(), PetscPythonInitialize(), PetscViewerPythonViewObject()

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerPythonCreate(MPI_Comm comm, const char pyname[], PetscViewer *viewer)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerType
```

---

## PetscViewerPythonGetType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPythonGetType/

**Contents:**
- PetscViewerPythonGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the Python name of a PetscViewer object implemented in Python.

pyname - full dotted Python name [package].module[.{class|function}]

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerType, PetscViewerCreate(), PetscViewerSetType(), PETSCVIEWERPYTHON, PetscPythonInitialize(), PetscViewerPythonSetType()

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerPythonGetType(PetscViewer viewer, const char *pyname[])
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerType
```

---

## PetscViewerPythonSetType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPythonSetType/

**Contents:**
- PetscViewerPythonSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Initialize a PetscViewer object implemented in Python.

viewer - the viewer object.

pyname - full dotted Python name [package].module[.{class|function}]

-viewer_python_type pyname - python class

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerType, PetscViewerCreate(), PetscViewerSetType(), PETSCVIEWERPYTHON, PetscPythonInitialize()

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerPythonSetType(PetscViewer viewer, const char pyname[])
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerType
```

---

## PetscViewerPythonViewObject#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerPythonViewObject/

**Contents:**
- PetscViewerPythonViewObject#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

viewer - the viewer object.

obj - the object to be viewed.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerPythonCreate()

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscObject
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerPythonViewObject(PetscViewer viewer, PetscObject obj)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerPythonCreate()
```

---

## PETSCVIEWERPYTHON#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERPYTHON/

**Contents:**
- PETSCVIEWERPYTHON#
- Notes#
- See Also#
- Level#
- Location#

A viewer implemented using Python code

This is the parent viewer for any implemented in Python.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), VecView(), DMView(), DMPLEX, PETSCVIEWERPYVISTA

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerCreate()
```

Example 3 (unknown):
```unknown
PETSCVIEWERPYVISTA
```

---

## PETSCVIEWERPYVISTA#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERPYVISTA/

**Contents:**
- PETSCVIEWERPYVISTA#
- Notes#
- See Also#
- Level#
- Location#

A PyVista viewer implemented using Python code

Currently the DM viewer only supports DMPLEX meshes.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), VecView(), DMView(), DMPLEX

src/sys/classes/viewer/impls/pyvista/pyvistaviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerCreate()
```

---

## PetscViewerReadable#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerReadable/

**Contents:**
- PetscViewerReadable#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return a flag whether the viewer can be read from with PetscViewerRead()

viewer - the PetscViewer context

flg - PETSC_TRUE if the viewer is readable, PETSC_FALSE otherwise

PETSC_TRUE means that viewer’s PetscViewerType supports reading, that is PetscViewerRead(), (this holds e.g. for PETSCVIEWERBINARY) and the viewer is in a mode allowing reading, i.e. PetscViewerFileGetMode() returns one of FILE_MODE_READ, FILE_MODE_UPDATE, FILE_MODE_APPEND_UPDATE.

Viewers: Looking at PETSc Objects, PetscViewerRead(), PetscViewer, PetscViewerWritable(), PetscViewerCheckReadable(), PetscViewerCreate(), PetscViewerFileSetMode(), PetscViewerFileSetType()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerRead()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerReadable(PetscViewer viewer, PetscBool *flg)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewerRead#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerRead/

**Contents:**
- PetscViewerRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Reads data from a PetscViewer

data - Location to write the data, treated as an array of the type defined by datatype

num - Number of items of data to read

dtype - Type of data to read

count - number of items of data actually read, or NULL

If datatype is PETSC_STRING and num is negative, reads until a newline character is found, until a maximum of (-num - 1) chars.

Only certain viewers, such as PETSCVIEWERBINARY can be read from, see PetscViewerReadable()

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), PetscViewerReadable(), PetscViewerBinaryGetDescriptor(), PetscViewerBinaryGetInfoPointer(), PetscFileMode

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerRead(PetscViewer viewer, void *data, PetscInt num, PetscInt *count, PetscDataType dtype)
```

Example 3 (unknown):
```unknown
PETSC_STRING
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PetscViewerRegisterAll#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerRegisterAll/

**Contents:**
- PetscViewerRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the viewer types (PetscViewerType) in the PetscViewer package.

Viewers: Looking at PETSc Objects, PetscViewer

src/sys/classes/viewer/interface/viewregall.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerType
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscViewerRegisterAll(void)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerRegister#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerRegister/

**Contents:**
- PetscViewerRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a viewer to those available for use with PetscViewerSetType()

Not Collective, No Fortran Support

sname - name of a new user-defined viewer

function - routine to create method context

PetscViewerRegister() may be called multiple times to add several user-defined viewers.

Then, your solver can be chosen with the procedural interface via

or at runtime via the option

Viewers: Looking at PETSc Objects, PetscViewerRegisterAll()

src/sys/classes/viewer/interface/viewreg.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerSetType()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerRegister(const char *sname, PetscErrorCode (*function)(PetscViewer))
```

Example 3 (unknown):
```unknown
PetscViewerRegister()
```

Example 4 (unknown):
```unknown
PetscViewerRegister("my_viewer_type", MyViewerCreate);
```

---

## PetscViewerRestoreSubViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerRestoreSubViewer/

**Contents:**
- PetscViewerRestoreSubViewer#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restores a PetscViewer obtained with PetscViewerGetSubViewer().

viewer - the PetscViewer that was reproduced

comm - the sub communicator

outviewer - the subviewer to be returned

Automatically runs PetscViewerFlush() on outviewer

Must be called by all MPI processes that share viewer, for processes that are not of interest you can pass PETSC_COMM_SELF.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscViewerGetSubViewer(), PetscViewerFlush()

src/sys/classes/viewer/interface/dupl.c

src/ts/tutorials/ex30.c src/vec/vec/tutorials/ex14f.F90 src/dm/tutorials/ex6.c src/vec/vec/tutorials/ex9f.F90

PetscViewerRestoreSubViewer_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerRestoreSubViewer_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerRestoreSubViewer_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerRestoreSubViewer_String() in src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerGetSubViewer()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerRestoreSubViewer(PetscViewer viewer, MPI_Comm comm, PetscViewer *outviewer)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerSAWsOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSAWsOpen/

**Contents:**
- PetscViewerSAWsOpen#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Opens an SAWs PetscViewer.

Collective; No Fortran Support

comm - the MPI communicator

lab - the PetscViewer

-saws_port port number - port number where you are running SAWs client

-xxx_view saws - publish the object xxx

-xxx_saws_block - blocks the program at the end of a critical point (for KSP and SNES it is the end of a solve) until the user unblocks the problem with an external tool that access the object with SAWS

Unlike other viewers that only access the object being viewed on the call to XXXView(object,viewer) the SAWs viewer allows one to view the object asynchronously as the program continues to run. One can remove SAWs access to the object with a call to PetscObjectSAWsViewOff().

Information about the SAWs is available via https://bitbucket.org/saws/saws

Viewers: Looking at PETSc Objects, PetscViewerDestroy(), PetscViewerStringSPrintf(), PETSC_VIEWER_SAWS_(), PetscObjectSAWsBlock(), PetscObjectSAWsViewOff(), PetscObjectSAWsTakeAccess(), PetscObjectSAWsGrantAccess()

src/sys/classes/viewer/impls/ams/amsopen.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"    
#include "petscviewersaws.h"    
PetscErrorCode PetscViewerSAWsOpen(MPI_Comm comm, PetscViewer *lab)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscObjectSAWsViewOff()
```

---

## PetscViewersCreate#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewersCreate/

**Contents:**
- PetscViewersCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a container to hold a set of PetscViewer’s. The container is essentially a sparse, growable in length array of PetscViewers

comm - the MPI communicator

v - the collection of PetscViewers

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewers, PetscViewerCreate(), PetscViewersDestroy()

src/sys/classes/viewer/interface/viewers.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscViewersCreate(MPI_Comm comm, PetscViewers *v)
```

Example 4 (unknown):
```unknown
PetscViewers
```

---

## PetscViewersDestroy#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewersDestroy/

**Contents:**
- PetscViewersDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a set of PetscViewers created with PetscViewersCreate().

v - the PetscViewers to be destroyed.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerDestroy(), PetscViewers, PetscViewerSocketOpen(), PetscViewerASCIIOpen(), PetscViewerCreate(), PetscViewerDrawOpen(), PetscViewersCreate()

src/sys/classes/viewer/interface/viewers.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewersCreate()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscViewersDestroy(PetscViewers *v)
```

Example 4 (unknown):
```unknown
PetscViewers
```

---

## PetscViewerSetFormat#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSetFormat/

**Contents:**
- PetscViewerSetFormat#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the format for a PetscViewer.

Logically Collective, No Fortran Support

This routine is deprecated, you should use PetscViewerPushFormat()/PetscViewerPopFormat()

viewer - the PetscViewer

See PetscViewerFormat for available values

Viewers: Looking at PETSc Objects, PetscViewerGetFormat(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), MatView(), VecView(), PetscViewerType, PetscViewerPushFormat(), PetscViewerPopFormat(), PetscViewerDrawOpen(), PetscViewerSocketOpen()

src/sys/classes/viewer/interface/viewa.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h" 
PetscErrorCode PetscViewerSetFormat(PetscViewer viewer, PetscViewerFormat format)
```

Example 3 (unknown):
```unknown
PetscViewerPushFormat()
```

Example 4 (unknown):
```unknown
PetscViewerPopFormat()
```

---

## PetscViewerSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSetFromOptions/

**Contents:**
- PetscViewerSetFromOptions#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets various options for a viewer based on values in the options database.

viewer - the viewer context

Must be called after PetscViewerCreate() but before the PetscViewer is used.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), PetscViewerSetType(), PetscViewerType

src/sys/classes/viewer/interface/viewreg.c

src/dm/tutorials/ex9.c src/tao/term/tutorials/ex1.c src/dm/tutorials/ex10.c src/mat/tutorials/ex10.c

PetscViewerSetFromOptions_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerSetFromOptions_ADIOS() in src/sys/classes/viewer/impls/adios/adios.c PetscViewerSetFromOptions_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerSetFromOptions_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerSetFromOptions_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerSetFromOptions_GLVis() in src/sys/classes/viewer/impls/glvis/glvis.c PetscViewerSetFromOptions_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c PetscViewerSetFromOptions_Socket() in src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerSetFromOptions(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewerCreate()
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSetOptionsPrefix/

**Contents:**
- PetscViewerSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for PetscViewer options in the database during PetscViewerSetFromOptions().

viewer - the PetscViewer context

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerSetFromOptions(), PetscViewerAppendOptionsPrefix()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerSetFromOptions()
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerSetOptionsPrefix(PetscViewer viewer, const char prefix[])
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerSetType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSetType/

**Contents:**
- PetscViewerSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Builds PetscViewer for a particular implementation.

viewer - the PetscViewer context obtained with PetscViewerCreate()

type - for example, PETSCVIEWERASCII

-viewer_type type - Sets the type; use -help for a list of available methods (for instance, ascii)

See PetscViewerType for possible values

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), PetscViewerGetType(), PetscViewerType, PetscViewerPushFormat()

src/sys/classes/viewer/interface/viewreg.c

src/ts/tutorials/ex11.c src/tao/term/tutorials/ex1.c src/dm/impls/plex/tutorials/ex1f90.F90 src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/dm/tutorials/ex21.c src/sys/classes/viewer/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex15.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerSetType(PetscViewer viewer, PetscViewerType type)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerCreate()
```

---

## PetscViewerSetUp#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSetUp/

**Contents:**
- PetscViewerSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets up the internal viewer data structures for the later use.

viewer - the PetscViewer context

For basic use of the PetscViewer classes the user need not explicitly call PetscViewerSetUp(), since these actions will happen automatically.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerCreate(), PetscViewerDestroy()

src/sys/classes/viewer/interface/view.c

src/tao/term/tutorials/ex1.c

PetscViewerSetUp_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerSetUp_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerSetUp(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerSetUp()
```

---

## PetscViewersGetViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewersGetViewer/

**Contents:**
- PetscViewersGetViewer#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets a PetscViewer from a PetscViewers collection

Collective if the viewer has not previously be obtained.

viewers - object created with PetscViewersCreate()

n - number of PetscViewer you want

viewer - the PetscViewer

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewers, PetscViewersCreate(), PetscViewersDestroy()

src/sys/classes/viewer/interface/viewers.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewers
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscViewersGetViewer(PetscViewers viewers, PetscInt n, PetscViewer *viewer)
```

Example 4 (unknown):
```unknown
PetscViewersCreate()
```

---

## PetscViewerSocketOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSocketOpen/

**Contents:**
- PetscViewerSocketOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Environmental variables#
- Notes#
- See Also#
- Level#
- Location#

Opens a connection to a MATLAB or other socket based server.

comm - the MPI communicator

machine - the machine the server is running on, use NULL for the local machine, use “server” to passively wait for a connection from elsewhere

port - the port to connect to, use PETSC_DEFAULT for the default

lab - a context to use when communicating with the server

For use with PETSC_VIEWER_SOCKET_WORLD, PETSC_VIEWER_SOCKET_SELF, PETSC_VIEWER_SOCKET_() or if NULL is passed for machine or PETSC_DEFAULT is passed for port

-viewer_socket_machine machine - the machine where the socket is available

-viewer_socket_port port - the socket to connect to

PETSC_VIEWER_SOCKET_MACHINE - machine name

PETSC_VIEWER_SOCKET_PORT - portnumber

Most users should employ the following commands to access the MATLAB PetscViewer

Currently the only socket client available is MATLAB, PETSc must be configured with –with-matlab for this client. See src/dm/tests/ex12.c and ex12.m for an example of usage.

The socket viewer is in some sense a subclass of the binary viewer, to read and write to the socket use PetscViewerBinaryRead(), PetscViewerBinaryWrite(), PetscViewerBinarWriteStringArray(), PetscViewerBinaryGetDescriptor().

Use this for communicating with an interactive MATLAB session, see PETSC_VIEWER_MATLAB_() for writing output to a .mat file. Use PetscMatlabEngineCreate() or PETSC_MATLAB_ENGINE_(), PETSC_MATLAB_ENGINE_SELF, or PETSC_MATLAB_ENGINE_WORLD for communicating with a MATLAB Engine

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PETSCVIEWERSOCKET, MatView(), VecView(), PetscViewerDestroy(), PetscViewerCreate(), PetscViewerSetType(), PetscViewerSocketSetConnection(), PETSC_VIEWER_SOCKET_, PETSC_VIEWER_SOCKET_WORLD, PETSC_VIEWER_SOCKET_SELF, PetscViewerBinaryWrite(), PetscViewerBinaryRead(), PetscViewerBinaryWriteStringArray(), PetscBinaryViewerGetDescriptor(), PetscMatlabEngineCreate()

src/sys/classes/viewer/impls/socket/send.c

src/vec/vec/tutorials/ex42a.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"  
PetscErrorCode PetscViewerSocketOpen(MPI_Comm comm, const char machine[], int port, PetscViewer *lab)
```

Example 2 (unknown):
```unknown
PETSC_DEFAULT
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_SOCKET_WORLD
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_SOCKET_SELF
```

---

## PetscViewerSocketSetConnection#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerSocketSetConnection/

**Contents:**
- PetscViewerSocketSetConnection#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the machine and port that a PETSc socket viewer is to use

v - viewer to connect

machine - host to connect to, use NULL for the local machine,use “server” to passively wait for a connection from elsewhere

port - the port on the machine one is connecting to, use PETSC_DEFAULT for default

Viewers: Looking at PETSc Objects, PETSCVIEWERMATLAB, PETSCVIEWERSOCKET, PetscViewerSocketOpen()

src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"  
PetscErrorCode PetscViewerSocketSetConnection(PetscViewer v, const char machine[], int port)
```

Example 2 (unknown):
```unknown
PETSC_DEFAULT
```

Example 3 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 4 (unknown):
```unknown
PETSCVIEWERSOCKET
```

---

## PETSCVIEWERSOCKET#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERSOCKET/

**Contents:**
- PETSCVIEWERSOCKET#
- See Also#
- Level#
- Location#

A viewer that writes to a Unix socket

Viewers: Looking at PETSc Objects, PETSC_VIEWERBINARY, PetscViewerSocketOpen(), PetscViewerDrawOpen(), PETSC_VIEWER_DRAW_(), PETSC_VIEWER_DRAW_SELF, PETSC_VIEWER_DRAW_WORLD, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PETSCVIEWERDRAW, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWERBINARY
```

Example 2 (unknown):
```unknown
PetscViewerSocketOpen()
```

Example 3 (unknown):
```unknown
PetscViewerDrawOpen()
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_DRAW_()
```

---

## PetscViewerStringGetStringRead#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerStringGetStringRead/

**Contents:**
- PetscViewerStringGetStringRead#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the string that a PETSCVIEWERSTRING uses

viewer - PETSCVIEWERSTRING viewer

string - the string, optional use NULL if you do not need

len - the length of the string, optional use NULL if you do not need it

Do not write to the string nor free it

Copies the current contents of the PETSCVIEWERSTRING viewer string

Viewers: Looking at PETSc Objects, PetscViewerStringOpen(), PETSCVIEWERSTRING, PetscViewerStringSetString(), PetscViewerStringSPrintf(), PetscViewerStringSetOwnString()

src/sys/classes/viewer/impls/string/stringv.c

src/ts/tutorials/ex3.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERSTRING
```

Example 2 (unknown):
```unknown
#include "petscsys.h"  
PetscErrorCode PetscViewerStringGetStringRead(PetscViewer viewer, const char *string[], size_t *len) PeNS
```

Example 3 (unknown):
```unknown
PETSCVIEWERSTRING
```

Example 4 (unknown):
```unknown
PETSCVIEWERSTRING
```

---

## PetscViewerStringOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerStringOpen/

**Contents:**
- PetscViewerStringOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Opens a string as a PETSCVIEWERSTRING PetscViewer. This is a very simple PetscViewer; information on the object is simply stored into the string in a fairly nice way.

Collective; No Fortran Support

comm - the communicator

string - the string to use

len - the string length

lab - the PetscViewer

Viewers: Looking at PETSc Objects, PETSCVIEWERSTRING, PetscViewerDestroy(), PetscViewerStringSPrintf(), PetscViewerStringGetStringRead(), PetscViewerStringSetString()

src/sys/classes/viewer/impls/string/stringv.c

src/ksp/ksp/tutorials/ex72.c src/ts/tutorials/ex3.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERSTRING
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
#include "petscsys.h"  
PetscErrorCode PetscViewerStringOpen(MPI_Comm comm, char string[], size_t len, PetscViewer *lab) PeNS
```

---

## PetscViewerStringSetOwnString#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerStringSetOwnString/

**Contents:**
- PetscViewerStringSetOwnString#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

tells the viewer that it now owns the string and is responsible for freeing it with PetscFree()

viewer - string viewer

If you call this the string must have been obtained with PetscMalloc() and you cannot free the string

Viewers: Looking at PETSc Objects, PetscViewerStringOpen(), PETSCVIEWERSTRING, PetscViewerStringGetStringRead(), PetscViewerStringSPrintf(), PetscViewerStringSetString()

src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFree()
```

Example 2 (unknown):
```unknown
#include "petscsys.h"  
PetscErrorCode PetscViewerStringSetOwnString(PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscMalloc()
```

Example 4 (unknown):
```unknown
PetscViewerStringOpen()
```

---

## PetscViewerStringSetString#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerStringSetString/

**Contents:**
- PetscViewerStringSetString#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

sets the string that a string viewer will print to

viewer - string viewer you wish to attach string to

string - the string to print data into

len - the length of the string

The function does not copy the string, it uses it directly therefore you cannot free the string until the viewer is destroyed. If you call PetscViewerStringSetOwnString() the ownership passes to the viewer and it will be responsible for freeing it. In this case the string must be obtained with PetscMalloc().

Viewers: Looking at PETSc Objects, PetscViewerStringOpen(), PETSCVIEWERSTRING, PetscViewerStringGetStringRead(), PetscViewerStringSPrintf(), PetscViewerStringSetOwnString()

src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"  
PetscErrorCode PetscViewerStringSetString(PetscViewer viewer, char string[], size_t len) PeNS
```

Example 2 (unknown):
```unknown
PetscViewerStringSetOwnString()
```

Example 3 (unknown):
```unknown
PetscMalloc()
```

Example 4 (unknown):
```unknown
PetscViewerStringOpen()
```

---

## PetscViewerStringSPrintf#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerStringSPrintf/

**Contents:**
- PetscViewerStringSPrintf#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Prints information to a PETSCVIEWERSTRING PetscViewer object

Logically Collective; No Fortran Support

viewer - a string PetscViewer, formed by PetscViewerStringOpen()

format - the format of the input

Though this is collective each MPI process maintains a separate string

Viewers: Looking at PETSc Objects, PETSCVIEWERSTRING, PetscViewerStringOpen(), PetscViewerStringGetStringRead(), PetscViewerStringSetString()

src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERSTRING
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (lua):
```lua
#include "petscsys.h"  
PetscErrorCode PetscViewerStringSPrintf(PetscViewer viewer, const char format[], ...)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSCVIEWERSTRING#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERSTRING/

**Contents:**
- PETSCVIEWERSTRING#
- See Also#
- Level#
- Location#

A viewer that writes to a string

Viewers: Looking at PETSc Objects, PetscViewerStringOpen(), PetscViewerStringSPrintf(), PetscViewerSocketOpen(), PetscViewerDrawOpen(), PETSCVIEWERSOCKET, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PETSCVIEWERDRAW, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/string/stringv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerStringOpen()
```

Example 2 (unknown):
```unknown
PetscViewerStringSPrintf()
```

Example 3 (unknown):
```unknown
PetscViewerSocketOpen()
```

Example 4 (unknown):
```unknown
PetscViewerDrawOpen()
```

---

## PetscViewers#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewers/

**Contents:**
- PetscViewers#
- Synopsis#
- See Also#
- Level#
- Location#

Abstract collection of PetscViewers. It is stored as an expandable array of viewers.

Viewers: Looking at PETSc Objects, PetscViewerCreate(), PetscViewerSetType(), PetscViewerType, PetscViewer, PetscViewersCreate(), PetscViewersGetViewer()

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (julia):
```julia
typedef struct _n_PetscViewers *PetscViewers;
```

Example 3 (unknown):
```unknown
PetscViewerCreate()
```

Example 4 (unknown):
```unknown
PetscViewerSetType()
```

---

## PetscViewerType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerType/

**Contents:**
- PetscViewerType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

String with the name of a PETSc PetscViewer implementation

Viewers: Looking at PETSc Objects, PetscViewerSetType(), PetscViewer, PetscViewerRegister(), PetscViewerCreate()

include/petscviewer.h

src/dm/impls/plex/tutorials/ex19.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
typedef const char *PetscViewerType;
#define PETSCVIEWERSOCKET      "socket"
#define PETSCVIEWERASCII       "ascii"
#define PETSCVIEWERBINARY      "binary"
#define PETSCVIEWERSTRING      "string"
#define PETSCVIEWERDRAW        "draw"
#define PETSCVIEWERVU          "vu"
#define PETSCVIEWERMATHEMATICA "mathematica"
#define PETSCVIEWERHDF5        "hdf5"
#define PETSCVIEWERVTK         "vtk"
#define PETSCVIEWERMATLAB      "matlab"
#define PETSCVIEWERSAWS        "saws"
#define PETSCVIEWERGLVIS       "glvis"
#define PETSCVIEWERADIOS       "adios"
#define PETSCVIEWEREXODUSII    "exodusii"
#define PETSCVIEWERCGNS        "cgns"
#define PETSCVIEWERPYTHON      "python"
#define PETSCVIEWERPYVISTA     "pyvista"
```

Example 3 (unknown):
```unknown
PetscViewerSetType()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerViewFromOptions/

**Contents:**
- PetscViewerViewFromOptions#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

View from the viewer based on options in the options database

A - the PetscViewer context

obj - Optional object that provides the prefix for the option names

name - command line option

See PetscObjectViewFromOptions() for details on the viewers and formats support via this interface

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerView, PetscObjectViewFromOptions(), PetscViewerCreate()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerViewFromOptions(PetscViewer A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerView#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerView/

**Contents:**
- PetscViewerView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Visualizes a viewer object.

v - the viewer to be viewed

viewer - visualization context

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerPushFormat(), PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscViewerSocketOpen(), PetscViewerBinaryOpen(), PetscViewerLoad()

src/sys/classes/viewer/interface/view.c

src/sys/classes/viewer/tutorials/ex2f.F90 src/sys/classes/viewer/tutorials/ex2.c

PetscViewerView_ExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c PetscViewerView_ASCII() in src/sys/classes/viewer/impls/ascii/filev.c PetscViewerView_Binary() in src/sys/classes/viewer/impls/binary/binv.c PetscViewerView_CGNS() in src/sys/classes/viewer/impls/cgns/cgnsv.c PetscViewerView_Draw() in src/sys/classes/viewer/impls/draw/drawv.c PetscViewerView_HDF5() in src/sys/classes/viewer/impls/hdf5/impl/ihdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerView(PetscViewer v, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerPushFormat()
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## PetscViewerVTKAddField#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKAddField/

**Contents:**
- PetscViewerVTKAddField#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Add a field to the viewer

viewer - PETSCVIEWERVTK

dm - DM on which Vec lives

PetscViewerVTKWriteFunction - function to write this Vec

fieldnum - which field of the DM to write (PETSC_DEFAULT if the whole vector should be written)

fieldtype - Either PETSC_VTK_POINT_FIELD or PETSC_VTK_CELL_FIELD

checkdm - whether to check for identical dm arguments as fields are added

vec - Vec from which to write

This routine keeps exclusive ownership of the Vec. The caller should not use or destroy the Vec after calling it.

Viewers: Looking at PETSc Objects, PETSCVIEWERVTK, PetscViewerVTKOpen(), DMDAVTKWriteAll(), PetscViewerVTKWriteFunction, PetscViewerVTKGetDM()

src/sys/classes/viewer/impls/vtk/vtkv.c

PetscViewerVTKAddField_VTK(PetscViewer viewer, PetscObject dm, PetscErrorCode (*PetscViewerVTKWriteFunction)() in src/sys/classes/viewer/impls/vtk/vtkv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerVTKAddField(PetscViewer viewer, PetscObject dm, PetscErrorCode (*PetscViewerVTKWriteFunction)(PetscObject, PetscViewer), PetscInt fieldnum, PetscViewerVTKFieldType fieldtype, PetscBool checkdm, PetscObject vec)
```

Example 2 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 3 (unknown):
```unknown
PETSC_DEFAULT
```

Example 4 (unknown):
```unknown
PETSC_VTK_POINT_FIELD
```

---

## PetscViewerVTKFieldType#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKFieldType/

**Contents:**
- PetscViewerVTKFieldType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Categorizes a field that is being written through a PETSCVIEWERVTK viewer so that the VTK writer can place it on the correct mesh entity and with the correct component layout

PETSC_VTK_INVALID - sentinel for an uninitialized entry

PETSC_VTK_POINT_FIELD - scalar (or generic multi-component) field stored at mesh points

PETSC_VTK_POINT_VECTOR_FIELD - vector-valued field stored at mesh points

PETSC_VTK_CELL_FIELD - scalar (or generic multi-component) field stored on mesh cells

PETSC_VTK_CELL_VECTOR_FIELD - vector-valued field stored on mesh cells

PETSCVIEWERVTK, PetscViewerVTKAddField(), PetscViewerVTKOpen(), PetscViewer

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 2 (unknown):
```unknown
typedef enum {
  PETSC_VTK_INVALID,
  PETSC_VTK_POINT_FIELD,
  PETSC_VTK_POINT_VECTOR_FIELD,
  PETSC_VTK_CELL_FIELD,
  PETSC_VTK_CELL_VECTOR_FIELD
} PetscViewerVTKFieldType;
```

Example 3 (unknown):
```unknown
PETSC_VTK_INVALID
```

Example 4 (unknown):
```unknown
PETSC_VTK_POINT_FIELD
```

---

## PetscViewerVTKFWrite#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKFWrite/

**Contents:**
- PetscViewerVTKFWrite#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

write binary data preceded by 32-bit int length (in bytes), does not do byte swapping.

viewer - logically collective viewer, data written from rank 0

fp - file pointer valid on rank 0

data - data pointer valid on rank 0

n - number of data items

If PetscScalar is __float128 then the binary files are written in double precision

Viewers: Looking at PETSc Objects, PETSCVIEWERVTK, DMDAVTKWriteAll(), DMPlexVTKWriteAll(), PetscViewerPushFormat(), PetscViewerVTKOpen(), PetscBinaryWrite()

src/sys/classes/viewer/impls/vtk/vtkv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerVTKFWrite(PetscViewer viewer, FILE *fp, const void *data, PetscCount n, MPI_Datatype dtype)
```

Example 2 (unknown):
```unknown
PetscScalar
```

Example 3 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 4 (unknown):
```unknown
DMDAVTKWriteAll()
```

---

## PetscViewerVTKGetDM#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKGetDM/

**Contents:**
- PetscViewerVTKGetDM#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

get the DM associated with the PETSCVIEWERVTK viewer

viewer - PETSCVIEWERVTK viewer

dm - DM associated with the viewer (as a PetscObject)

Viewers: Looking at PETSc Objects, PETSCVIEWERVTK, PetscViewerVTKOpen(), DMDAVTKWriteAll(), PetscViewerVTKWriteFunction, PetscViewerVTKAddField()

src/sys/classes/viewer/impls/vtk/vtkv.c

PetscViewerVTKGetDM_VTK() in src/sys/classes/viewer/impls/vtk/vtkv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerVTKGetDM(PetscViewer viewer, PetscObject *dm)
```

Example 3 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## PetscViewerVTKOpen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKOpen/

**Contents:**
- PetscViewerVTKOpen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Opens a PETSCVIEWERVTK viewer file.

comm - MPI communicator

vtk - PetscViewer for VTK input/output to use with the specified file

Viewers: Looking at PETSc Objects, PETSCVIEWERVTK, PetscViewerASCIIOpen(), PetscViewerPushFormat(), PetscViewerDestroy(), VecView(), MatView(), VecLoad(), MatLoad(), PetscFileMode, PetscViewer

src/sys/classes/viewer/impls/vtk/vtkv.c

src/snes/tutorials/ex16.c src/dm/impls/stag/tutorials/ex4.c src/ksp/ksp/tutorials/ex42.c src/dm/impls/stag/tutorials/ex6.c src/snes/tutorials/ex15.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerVTKOpen(MPI_Comm comm, const char name[], PetscFileMode type, PetscViewer *vtk)
```

Example 3 (bash):
```bash
FILE_MODE_WRITE - create new file for binary output
  FILE_MODE_READ - open existing file for binary input (not currently supported)
  FILE_MODE_APPEND - open existing file for binary output (not currently supported)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerVTKWriteFunction#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVTKWriteFunction/

**Contents:**
- PetscViewerVTKWriteFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

functional form used to provide a writer to the PETSCVIEWERVTK

object - the PETSc object to be written

viewer - viewer it is to be written to

Viewers: Looking at PETSc Objects, PETSCVIEWERVTK, PetscViewerVTKAddField()

src/sys/classes/viewer/impls/vtk/vtkv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 2 (cpp):
```cpp
#include <petscviewer.h>
PetscViewerVTKWriteFunction(PetscObject object,PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 4 (unknown):
```unknown
PetscViewerVTKAddField()
```

---

## PETSCVIEWERVTK#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERVTK/

**Contents:**
- PETSCVIEWERVTK#
- See Also#
- Level#
- Location#
- Examples#

A viewer that writes to a VTK file

Viewers: Looking at PETSc Objects, PetscViewerVTKOpen(), PetscViewerHDF5Open(), PetscViewerStringSPrintf(), PetscViewerSocketOpen(), PetscViewerDrawOpen(), PETSCVIEWERSOCKET, PetscViewerCreate(), PetscViewerASCIIOpen(), PetscViewerBinaryOpen(), PETSCVIEWERBINARY, PETSCVIEWERDRAW, PETSCVIEWERSTRING, PetscViewerMatlabOpen(), VecView(), DMView(), PetscViewerMatlabPutArray(), PETSCVIEWERASCII, PETSCVIEWERMATLAB, PetscViewerFileSetName(), PetscViewerFileSetMode(), PetscViewerFormat, PetscViewerType, PetscViewerSetType()

src/sys/classes/viewer/impls/vtk/vtkv.c

src/dm/impls/plex/tutorials/ex1f90.F90 src/ts/tutorials/ex11.c src/ksp/ksp/tutorials/ex70.c src/dm/tutorials/ex21.c src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex20.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerVTKOpen()
```

Example 2 (unknown):
```unknown
PetscViewerHDF5Open()
```

Example 3 (unknown):
```unknown
PetscViewerStringSPrintf()
```

Example 4 (unknown):
```unknown
PetscViewerSocketOpen()
```

---

## PetscViewerVUFlushDeferred#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUFlushDeferred/

**Contents:**
- PetscViewerVUFlushDeferred#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Flushes the deferred write cache to the file.

viewer - The PETSCVIEWERVU PetscViewer

Viewers: Looking at PETSc Objects, PETSCVIEWERVU, PetscViewerVUPrintDeferred()

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerVUFlushDeferred(PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSCVIEWERVU
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERVU
```

---

## PetscViewerVUGetPointer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUGetPointer/

**Contents:**
- PetscViewerVUGetPointer#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Extracts the file pointer from a PETSCVIEWERVU PetscViewer.

viewer - The PetscViewer

fd - The file pointer

Viewers: Looking at PETSc Objects, PETSCVIEWERVU, PetscViewerASCIIGetPointer()

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERVU
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerVUGetPointer(PetscViewer viewer, FILE **fd)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerVUGetVecSeen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUGetVecSeen/

**Contents:**
- PetscViewerVUGetVecSeen#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the flag which indicates whether we have viewed a vector. This is usually called internally rather than by a user.

viewer - The PETSCVIEWERVU PetscViewer

vecSeen - The flag which indicates whether we have viewed a vector

Viewers: Looking at PETSc Objects, PETSCVIEWERVU

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerVUGetVecSeen(PetscViewer viewer, PetscBool *vecSeen)
```

Example 2 (unknown):
```unknown
PETSCVIEWERVU
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERVU
```

---

## PetscViewerVUPrintDeferred#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUPrintDeferred/

**Contents:**
- PetscViewerVUPrintDeferred#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Prints to the deferred write cache instead of the file.

viewer - The PETSCVIEWERVU PetscViewer

format - The format string

Viewers: Looking at PETSc Objects, PETSCVIEWERVU, PetscViewerVUFlushDeferred()

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (lua):
```lua
#include "petscsys.h"   
PetscErrorCode PetscViewerVUPrintDeferred(PetscViewer viewer, const char format[], ...)
```

Example 2 (unknown):
```unknown
PETSCVIEWERVU
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERVU
```

---

## PetscViewerVUSetMode#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUSetMode/

**Contents:**
- PetscViewerVUSetMode#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the mode in which to open the file.

viewer - The PetscViewer

Use PetscViewerFileSetMode() instead.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerFileSetMode()

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_DEPRECATED_FUNCTION(3, 15, 0, "PetscViewerFileSetMode()", ) static inline PetscErrorCode PetscViewerVUSetMode(PetscViewer viewer, PetscFileMode mode)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewerFileSetMode()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscViewerVUSetVecSeen#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerVUSetVecSeen/

**Contents:**
- PetscViewerVUSetVecSeen#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the flag which indicates whether we have viewed a vector. This is usually called internally rather than by a user.

viewer - The PETSCVIEWERVU PetscViewer

vecSeen - The flag which indicates whether we have viewed a vector

Viewers: Looking at PETSc Objects, PETSCVIEWERVU, PetscViewerVUGetVecSeen()

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsys.h"   
PetscErrorCode PetscViewerVUSetVecSeen(PetscViewer viewer, PetscBool vecSeen)
```

Example 2 (unknown):
```unknown
PETSCVIEWERVU
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERVU
```

---

## PETSCVIEWERVU#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSCVIEWERVU/

**Contents:**
- PETSCVIEWERVU#
- See Also#
- Level#
- Location#

A viewer that prints to a VU file

Viewers: Looking at PETSc Objects, PetscViewerVUFlushDeferred(), PetscViewerVUGetPointer(), PetscViewerVUSetVecSeen(), PetscViewerVUGetVecSeen(), PetscViewerVUPrintDeferred()

src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerVUFlushDeferred()
```

Example 2 (unknown):
```unknown
PetscViewerVUGetPointer()
```

Example 3 (unknown):
```unknown
PetscViewerVUSetVecSeen()
```

Example 4 (unknown):
```unknown
PetscViewerVUGetVecSeen()
```

---

## PetscViewerWritable#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewerWritable/

**Contents:**
- PetscViewerWritable#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return a flag whether the viewer can be written to with PetscViewerWrite()

viewer - the PetscViewer context

flg - PETSC_TRUE if the viewer is writable, PETSC_FALSE otherwise

PETSC_TRUE means viewer is in a mode allowing writing, i.e. PetscViewerFileGetMode() returns one of FILE_MODE_WRITE, FILE_MODE_APPEND, FILE_MODE_UPDATE, FILE_MODE_APPEND_UPDATE.

Viewers: Looking at PETSc Objects, PetscViewer, PetscViewerReadable(), PetscViewerCheckWritable(), PetscViewerCreate(), PetscViewerFileSetMode(), PetscViewerFileSetType()

src/sys/classes/viewer/interface/view.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerWrite()
```

Example 2 (unknown):
```unknown
#include "petscviewer.h" 
PetscErrorCode PetscViewerWritable(PetscViewer viewer, PetscBool *flg)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscViewer#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscViewer/

**Contents:**
- PetscViewer#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object for displaying in ASCII, saving to a binary file, graphically displaying, etc. PETSc objects and their data

Each PETSc class, for example Vec, has a viewer method associated with that class, for example VecView(), that can be used to view, display, store to a file information about that object, etc. Each class also has a method that uses the options database to view the object, for example VecViewFromOptions().

See PetscViewerType for a list of all PetscViewer types.

Viewers: Looking at PETSc Objects, PetscViewerType, PETSCVIEWERASCII, PetscViewerCreate(), PetscViewerSetType(), VecView(), VecViewFromOptions(), PetscObjectView()

include/petscviewertypes.h

src/mat/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/mat/tutorials/ex16.c src/snes/tutorials/ex70.c src/mat/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c

_p_PetscViewer in include/petsc/private/viewerimpl.h PetscViewer_ADIOS in include/petsc/private/vieweradiosimpl.h PetscViewer_CGNS in include/petsc/private/viewercgnsimpl.h PetscViewer_ExodusII in include/petsc/private/viewerexodusiiimpl.h PetscViewer_ASCII in src/sys/classes/viewer/impls/ascii/asciiimpl.h PetscViewer_Binary in src/sys/classes/viewer/impls/binary/binv.c PetscViewer_Draw in src/sys/classes/viewer/impls/draw/vdraw.h PetscViewer_Mathematica in src/sys/classes/viewer/impls/mathematica/mathematica.h PetscViewer_Matlab in src/sys/classes/viewer/impls/matlab/vmatlab.c PetscViewer_Socket in src/sys/classes/viewer/impls/socket/socket.h PetscViewer_String in src/sys/classes/viewer/impls/string/stringv.c PetscViewer_VTK in src/sys/classes/viewer/impls/vtk/vtkvimpl.h PetscViewer_VU in src/sys/classes/viewer/impls/vu/petscvu.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscViewer *PetscViewer;
```

Example 2 (unknown):
```unknown
VecViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscViewerType
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscVTKIntCast#

**URL:** https://petsc.org/release/manualpages/Viewer/PetscVTKIntCast/

**Contents:**
- PetscVTKIntCast#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

casts to a PetscVTKInt (which may be 32-bits in size), generates an error if the PetscVTKInt is not large enough to hold the number.

Not Collective; No Fortran Support

a - the value to cast

b - the resulting PetscVTKInt value

PetscBLASInt, PetscMPIInt, PetscInt, PetscBLASIntCast(), PetscIntCast()

src/sys/classes/viewer/impls/vtk/vtkvimpl.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscVTKInt
```

Example 2 (unknown):
```unknown
PetscVTKInt
```

Example 3 (unknown):
```unknown
#include "petscsys.h"   
static inline PetscErrorCode PetscVTKIntCast(PetscCount a, PetscVTKInt *b)
```

Example 4 (unknown):
```unknown
PetscVTKInt
```

---

## PetscXIOErrorHandlerFn#

**URL:** https://petsc.org/release/manualpages/Draw/PetscXIOErrorHandlerFn/

**Contents:**
- PetscXIOErrorHandlerFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

Function type for the X11 I/O error handler installed by PetscSetXIOErrorHandler(), called when the X server connection is lost

display - the X Display * whose connection has failed (passed as void * to avoid pulling in X headers)

By default PETSc installs a handler that gracefully aborts the program rather than letting Xlib call exit().

PetscDraw, PetscSetXIOErrorHandler()

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSetXIOErrorHandler()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void                    PetscXIOErrorHandlerFn(void *display);
```

Example 3 (unknown):
```unknown
PetscSetXIOErrorHandler()
```

---

## PETSC_DRAW_IMAGE#

**URL:** https://petsc.org/release/manualpages/Draw/PETSC_DRAW_IMAGE/

**Contents:**
- PETSC_DRAW_IMAGE#
- Options Database Keys#
- See Also#
- Level#
- Location#

PETSc graphics device that uses a raster buffer

-draw_size w,h - size of image in pixels

PetscDrawOpenImage(), PetscDrawSetFromOptions()

src/sys/classes/draw/impls/image/drawimage.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawOpenImage()
```

Example 2 (unknown):
```unknown
PetscDrawSetFromOptions()
```

---

## PETSC_DRAW_NULL#

**URL:** https://petsc.org/release/manualpages/Draw/PETSC_DRAW_NULL/

**Contents:**
- PETSC_DRAW_NULL#
- Note#
- See Also#
- Level#
- Location#

PETSc graphics device that ignores all draw commands

A PETSC_DRAW_NULL is useful in places where PetscDraw routines are called but no graphics window, for example, is available.

PetscDraw, PetscDrawOpenNull(), PETSC_DRAW_X, PetscDrawOpenNull(), PetscDrawIsNull()

src/sys/classes/draw/impls/null/drawnull.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_DRAW_NULL
```

Example 2 (unknown):
```unknown
PetscDrawOpenNull()
```

Example 3 (unknown):
```unknown
PETSC_DRAW_X
```

Example 4 (unknown):
```unknown
PetscDrawOpenNull()
```

---

## PETSC_DRAW_X#

**URL:** https://petsc.org/release/manualpages/Draw/PETSC_DRAW_X/

**Contents:**
- PETSC_DRAW_X#
- Options Database Keys#
- See Also#
- Level#
- Location#

PETSc graphics device that uses either X windows or its virtual version Xvfb

-display display - sets the display to use

-x_virtual - forces use of a X virtual display Xvfb that will not display anything but -draw_save will still work. Xvfb is automatically started up in PetscSetDisplay() with this option

-draw_size w,h - percentage of screen (either 1, .5, .3, .25), or size in pixels

-geometry x,y,w,h - set location and size in pixels

-draw_virtual - do not open a window (draw on a pixmap), -draw_save will still work

-draw_double_buffer - avoid window flickering (draw on pixmap and flush to window)

PetscDraw, PetscDrawOpenX(), PetscDrawSetDisplay(), PetscDrawSetFromOptions()

src/sys/classes/draw/impls/x/xops.c

Index of all Draw routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawOpenX()
```

Example 2 (unknown):
```unknown
PetscDrawSetDisplay()
```

Example 3 (unknown):
```unknown
PetscDrawSetFromOptions()
```

---

## PETSC_MATLAB_ENGINE_SELF#

**URL:** https://petsc.org/release/manualpages/Matlab/PETSC_MATLAB_ENGINE_SELF/

**Contents:**
- PETSC_MATLAB_ENGINE_SELF#
- See Also#
- Level#
- Location#

same as PETSC_MATLAB_ENGINE_(PETSC_COMM_SELF)

PetscMatlabEngine, PETSC_MATLAB_ENGINE_(), PETSC_MATLAB_ENGINE_WORLD

include/petscmatlab.h

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscMatlabEngine
```

Example 2 (unknown):
```unknown
PETSC_MATLAB_ENGINE_()
```

Example 3 (unknown):
```unknown
PETSC_MATLAB_ENGINE_WORLD
```

---

## PETSC_MATLAB_ENGINE_WORLD#

**URL:** https://petsc.org/release/manualpages/Matlab/PETSC_MATLAB_ENGINE_WORLD/

**Contents:**
- PETSC_MATLAB_ENGINE_WORLD#
- See Also#
- Level#
- Location#

same as PETSC_MATLAB_ENGINE_(PETSC_COMM_WORLD)

PetscMatlabEngine, PETSC_MATLAB_ENGINE_(), PETSC_MATLAB_ENGINE_SELF

include/petscmatlab.h

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscMatlabEngine
```

Example 2 (unknown):
```unknown
PETSC_MATLAB_ENGINE_()
```

Example 3 (unknown):
```unknown
PETSC_MATLAB_ENGINE_SELF
```

---

## PETSC_MATLAB_ENGINE_#

**URL:** https://petsc.org/release/manualpages/Matlab/PETSC_MATLAB_ENGINE_/

**Contents:**
- PETSC_MATLAB_ENGINE_#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Creates a MATLAB engine on each process in a communicator.

comm - the MPI communicator to share the engine

-matlab_engine_host - hostname on which to run MATLAB, one must be able to ssh to this host

Unlike almost all other PETSc routines, this does not return an error code. Usually used in the form

PetscMatlabEngineDestroy(), PetscMatlabEnginePut(), PetscMatlabEngineGet(), PetscMatlabEngineEvaluate(), PetscMatlabEngineGetOutput(), PetscMatlabEnginePrintOutput(), PetscMatlabEngineCreate(), PetscMatlabEnginePutArray(), PetscMatlabEngineGetArray(), PetscMatlabEngine, PETSC_MATLAB_ENGINE_WORLD, PETSC_MATLAB_ENGINE_SELF

src/sys/classes/matlabengine/matlab.c

Index of all Matlab routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscmatlab.h"  
PetscMatlabEngine PETSC_MATLAB_ENGINE_(MPI_Comm comm)
```

Example 2 (unknown):
```unknown
PetscMatlabEngineYYY(XXX object, PETSC_MATLAB_ENGINE_(comm));
```

Example 3 (unknown):
```unknown
PetscMatlabEngineDestroy()
```

Example 4 (unknown):
```unknown
PetscMatlabEnginePut()
```

---

## PETSC_VIEWER_BINARY_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_BINARY_SELF/

**Contents:**
- PETSC_VIEWER_BINARY_SELF#
- Level#
- Location#

same as PETSC_VIEWER_BINARY_(PETSC_COMM_SELF)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_BINARY_
```

---

## PETSC_VIEWER_BINARY_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_BINARY_WORLD/

**Contents:**
- PETSC_VIEWER_BINARY_WORLD#
- Level#
- Location#
- Examples#

same as PETSC_VIEWER_BINARY_(PETSC_COMM_WORLD)

include/petscviewer.h

src/sys/tutorials/ex5f90.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_BINARY_
```

---

## PETSC_VIEWER_BINARY_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_BINARY_/

**Contents:**
- PETSC_VIEWER_BINARY_#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Environmental variable#
- Notes#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERBINARY PetscViewer shared by all processes in a communicator.

comm - the MPI communicator to share the PETSCVIEWERBINARY

-viewer_binary_filename name - filename in which to store the binary data, defaults to binaryoutput

-viewer_binary_skip_info - true means do not create .info file for this viewer

-viewer_binary_skip_options - true means do not use the options database for this viewer

-viewer_binary_skip_header - true means do not store the usual header information in the binary file

-viewer_binary_mpiio - true means use the file via MPI-IO, maybe faster for large files and many MPI ranks

PETSC_VIEWER_BINARY_FILENAME - filename in which to store the binary data, defaults to binaryoutput

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, PETSC_VIEWER_BINARY_ does not return an error code. The binary PetscViewer is usually used in the form

Viewers: Looking at PETSc Objects, PETSCVIEWERBINARY, PETSC_VIEWER_BINARY_WORLD, PETSC_VIEWER_BINARY_SELF, PetscViewerBinaryOpen(), PetscViewerCreate(), PetscViewerDestroy()

src/sys/classes/viewer/impls/binary/binv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
PetscViewer PETSC_VIEWER_BINARY_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PETSCVIEWERBINARY
```

---

## PETSC_VIEWER_DRAW_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_DRAW_SELF/

**Contents:**
- PETSC_VIEWER_DRAW_SELF#
- Level#
- Location#

same as PETSC_VIEWER_DRAW_(PETSC_COMM_SELF)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_DRAW_
```

---

## PETSC_VIEWER_DRAW_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_DRAW_WORLD/

**Contents:**
- PETSC_VIEWER_DRAW_WORLD#
- Level#
- Location#
- Examples#

same as PETSC_VIEWER_DRAW_(PETSC_COMM_WORLD)

include/petscviewer.h

src/ts/tutorials/ex9.c src/ksp/ksp/tutorials/ex72.c src/ksp/ksp/tutorials/ex100f.F90 src/dm/tutorials/ex4.c src/ksp/ksp/tutorials/ex100.c src/snes/tutorials/ex19.c src/snes/tutorials/ex33.c src/ts/tutorials/ex10.c src/ksp/ksp/tutorials/ex28.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_DRAW_
```

---

## PETSC_VIEWER_DRAW_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_DRAW_/

**Contents:**
- PETSC_VIEWER_DRAW_#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a window PETSCVIEWERDRAW PetscViewer shared by all processors in an MPI communicator.

comm - the MPI communicator to share the window PetscViewer

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, PETSC_VIEWER_DRAW_() does not return an error code. The window is usually used in the form

Viewers: Looking at PETSc Objects, PETSCVIEWERDRAW, PetscViewer, PETSC_VIEWER_DRAW_WORLD, PETSC_VIEWER_DRAW_SELF, PetscViewerDrawOpen(),

src/sys/classes/viewer/impls/draw/drawv.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERDRAW
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscdraw.h" 
#include "petscviewer.h" 
PetscViewer PETSC_VIEWER_DRAW_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSC_VIEWER_GLVIS_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_GLVIS_/

**Contents:**
- PETSC_VIEWER_GLVIS_#
- Synopsis#
- Input Parameter#
- Environmental variables#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERGLVIS PetscViewer shared by all processors in a communicator.

Collective; No Fortran Support

comm - the MPI communicator to share the PETSCVIEWERGLVIS PetscViewer

PETSC_VIEWER_GLVIS_FILENAME - output filename (if specified dump to disk, and takes precedence on PETSC_VIEWER_GLVIS_HOSTNAME)

PETSC_VIEWER_GLVIS_HOSTNAME - machine where the GLVis server is listening (defaults to localhost)

PETSC_VIEWER_GLVIS_PORT - port opened by the GLVis server (defaults to 19916)

Unlike almost all other PETSc routines, PETSC_VIEWER_GLVIS_() does not return an error code. It is usually used in the form

How come this viewer is not stashed as an attribute in the MPI communicator?

Viewers: Looking at PETSc Objects, PETSCVIEWERGLVIS, PetscViewer, PetscViewerGLVISOpen(), PetscViewerGLVisType, PetscViewerCreate(), PetscViewerDestroy()

src/sys/classes/viewer/impls/glvis/glvis.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERGLVIS
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h" 
#include "petscsys.h"    
PetscViewer PETSC_VIEWER_GLVIS_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PETSCVIEWERGLVIS
```

---

## PETSC_VIEWER_HDF5_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_HDF5_/

**Contents:**
- PETSC_VIEWER_HDF5_#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Environmental variable#
- Note#
- See Also#
- Level#
- Location#

Creates an PETSCVIEWERHDF5 PetscViewer shared by all processors in a communicator.

comm - the MPI communicator to share the PETSCVIEWERHDF5 PetscViewer

-viewer_hdf5_filename name - name of the HDF5 file

PETSC_VIEWER_HDF5_FILENAME - name of the HDF5 file

Unlike almost all other PETSc routines, PETSC_VIEWER_HDF5_() does not return an error code. The HDF5 PetscViewer is usually used in the form

Viewers: Looking at PETSc Objects, PETSCVIEWERHDF5, PetscViewerHDF5Open(), PetscViewerCreate(), PetscViewerDestroy()

src/sys/classes/viewer/impls/hdf5/hdf5v.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscViewer PETSC_VIEWER_HDF5_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## PETSC_VIEWER_MATLAB_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_MATLAB_SELF/

**Contents:**
- PETSC_VIEWER_MATLAB_SELF#
- Level#
- Location#

same as PETSC_VIEWER_MATLAB_(PETSC_COMM_SELF)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_MATLAB_
```

---

## PETSC_VIEWER_MATLAB_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_MATLAB_WORLD/

**Contents:**
- PETSC_VIEWER_MATLAB_WORLD#
- Level#
- Location#

same as PETSC_VIEWER_MATLAB_(PETSC_COMM_WORLD)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_MATLAB_
```

---

## PETSC_VIEWER_MATLAB_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_MATLAB_/

**Contents:**
- PETSC_VIEWER_MATLAB_#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Environmental variable#
- Notes#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERMATLAB PetscViewer shared by all processors in a communicator.

comm - the MPI communicator to share the MATLAB PetscViewer

-viewer_matlab_filename name - name of the MATLAB file

PETSC_VIEWER_MATLAB_FILENAME - name of the MATLAB file

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, PETSC_VIEWER_MATLAB_() does not return an error code. The MATLAB PetscViewer is usually used in the form XXXView(XXX object, PETSC_VIEWER_MATLAB_(comm))

Use PETSC_VIEWER_SOCKET_() or PetscViewerSocketOpen() to communicator with an interactive MATLAB session.

PETSC_VIEWER_MATLAB_WORLD, PETSC_VIEWER_MATLAB_SELF, PetscViewerMatlabOpen(), PetscViewerCreate(), PetscViewerDestroy()

src/sys/classes/viewer/impls/matlab/vmatlab.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERMATLAB
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
#include "petscmat.h"      
PetscViewer PETSC_VIEWER_MATLAB_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSC_VIEWER_PYTHON_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_PYTHON_/

**Contents:**
- PETSC_VIEWER_PYTHON_#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a Python PetscViewer shared by all MPI processes in a communicator.

comm - the MPI communicator to share the PetscViewer

Unlike almost all other PETSc routines, PETSC_VIEWER_PYTHON_() does not return an error code. It is usually used in the form .vb XXXView(XXX object, PETSC_VIEWER_PYTHON_(comm)); .ve

Viewers: Looking at PETSc Objects, PetscViewer

src/sys/classes/viewer/impls/python/pythonviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscViewer PETSC_VIEWER_PYTHON_(MPI_Comm comm)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_PYTHON_()
```

---

## PETSC_VIEWER_PYVISTA_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_PYVISTA_/

**Contents:**
- PETSC_VIEWER_PYVISTA_#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a PyVista PetscViewer shared by all MPI processes in a communicator.

comm - the MPI communicator to share the PetscViewer

Unlike almost all other PETSc routines, PETSC_VIEWER_PYVISTA_() does not return an error code. It is usually used in the form .vb XXXView(XXX object, PETSC_VIEWER_PYVISTA_(comm)); .ve

Viewers: Looking at PETSc Objects, PetscViewer

src/sys/classes/viewer/impls/pyvista/pyvistaviewer.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscsys.h"   
PetscViewer PETSC_VIEWER_PYVISTA_(MPI_Comm comm)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_PYVISTA_()
```

---

## PETSC_VIEWER_SAWS_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SAWS_/

**Contents:**
- PETSC_VIEWER_SAWS_#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a SAWs PetscViewer shared by all MPI processes in a communicator.

comm - the MPI communicator to share the PetscViewer

Unlike almost all other PETSc routines, PETSC_VIEWER_SAWS_() does not return an error code. The resulting PetscViewer is usually used in the form

Viewers: Looking at PETSc Objects, PetscViewer, PETSC_VIEWER_SAWS_WORLD, PETSC_VIEWER_SAWS_SELF

src/sys/classes/viewer/impls/ams/ams.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewer PETSC_VIEWER_SAWS_(MPI_Comm comm)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_SAWS_()
```

---

## PETSC_VIEWER_SOCKET_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SOCKET_SELF/

**Contents:**
- PETSC_VIEWER_SOCKET_SELF#
- Level#
- Location#

same as PETSC_VIEWER_SOCKET_(PETSC_COMM_SELF)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_SOCKET_
```

---

## PETSC_VIEWER_SOCKET_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SOCKET_WORLD/

**Contents:**
- PETSC_VIEWER_SOCKET_WORLD#
- Level#
- Location#

same as PETSC_VIEWER_SOCKET_(PETSC_COMM_WORLD)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_SOCKET_
```

---

## PETSC_VIEWER_SOCKET_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_SOCKET_/

**Contents:**
- PETSC_VIEWER_SOCKET_#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Environmental variables#
- Notes#
- See Also#
- Level#
- Location#

Creates a socket viewer shared by all processors in a communicator.

comm - the MPI communicator to share the PETSCVIEWERSOCKET PetscViewer

For use with the default PETSC_VIEWER_SOCKET_WORLD or if NULL is passed for machine or PETSC_DEFAULT is passed for port

-viewer_socket_machine machine - machine to connect to

-viewer_socket_port port - port to connect to

PETSC_VIEWER_SOCKET_PORT - portnumber

PETSC_VIEWER_SOCKET_MACHINE - machine name

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, PETSC_VIEWER_SOCKET_() does not return an error code, it returns NULL if it fails. The PETSCVIEWERSOCKET PetscViewer is usually used in the form XXXView(XXX object, PETSC_VIEWER_SOCKET_(comm))

Currently the only socket client available is MATLAB. See src/dm/tests/ex12.c and ex12.m for an example of usage.

Connects to a waiting socket and stays connected until PetscViewerDestroy() is called.

Use this for communicating with an interactive MATLAB session, see PETSC_VIEWER_MATLAB_() for writing output to a .mat file. Use PetscMatlabEngineCreate() or PETSC_MATLAB_ENGINE_(), PETSC_MATLAB_ENGINE_SELF, or PETSC_MATLAB_ENGINE_WORLD for communicating with a MATLAB Engine

Viewers: Looking at PETSc Objects, PETSCVIEWERMATLAB, PETSCVIEWERSOCKET, PETSC_VIEWER_SOCKET_WORLD, PETSC_VIEWER_SOCKET_SELF, PetscViewerSocketOpen(), PetscViewerCreate(), PetscViewerSocketSetConnection(), PetscViewerDestroy(), PETSC_VIEWER_SOCKET_(), PetscViewerBinaryWrite(), PetscViewerBinaryRead(), PetscViewerBinaryWriteStringArray(), PetscViewerBinaryGetDescriptor(), PETSC_VIEWER_MATLAB_()

src/sys/classes/viewer/impls/socket/send.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscviewer.h"  
PetscViewer PETSC_VIEWER_SOCKET_(MPI_Comm comm)
```

Example 2 (unknown):
```unknown
PETSCVIEWERSOCKET
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_SOCKET_WORLD
```

---

## PETSC_VIEWER_STDERR_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDERR_SELF/

**Contents:**
- PETSC_VIEWER_STDERR_SELF#
- Level#
- Location#
- Examples#

same as PETSC_VIEWER_STDERR_(PETSC_COMM_SELF)

include/petscviewer.h

src/dm/impls/plex/tutorials/ex8.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDERR_
```

---

## PETSC_VIEWER_STDERR_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDERR_WORLD/

**Contents:**
- PETSC_VIEWER_STDERR_WORLD#
- Level#
- Location#

same as PETSC_VIEWER_STDERR_(PETSC_COMM_WORLD)

include/petscviewer.h

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDERR_
```

---

## PETSC_VIEWER_STDERR_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDERR_/

**Contents:**
- PETSC_VIEWER_STDERR_#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERASCII PetscViewer shared by all MPI processes in a communicator.

comm - the MPI communicator to share the PetscViewer

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, this does not return an error code. Usually used in the form

PetscViewerASCIIGetStderr() is preferred since it allows error checking

Viewers: Looking at PETSc Objects, PETSC_VIEWER_DRAW_, PetscViewerASCIIOpen(), PETSC_VIEWER_STDOUT_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, PETSC_VIEWER_STDERR_WORLD, PETSC_VIEWER_STDERR_SELF

src/sys/classes/viewer/impls/ascii/vcreatea.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
PetscViewer PETSC_VIEWER_STDERR_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PETSC_VIEWER_STDOUT_SELF#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDOUT_SELF/

**Contents:**
- PETSC_VIEWER_STDOUT_SELF#
- Level#
- Location#
- Examples#

same as PETSC_VIEWER_STDOUT_(PETSC_COMM_SELF)

include/petscviewer.h

src/vec/vec/tutorials/ex6.c src/vec/vec/tutorials/ex21f90.F90 src/vec/is/is/tutorials/ex2f.F90 src/vec/is/is/tutorials/ex1.c src/vec/vec/tutorials/ex4f.F90 src/mat/tutorials/ex12.c src/ksp/ksp/tutorials/ex62.c src/ksp/ksp/tutorials/ex8.c src/vec/vec/tutorials/ex6f.F90 src/vec/vec/tutorials/ex4f90.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDOUT_
```

---

## PETSC_VIEWER_STDOUT_WORLD#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDOUT_WORLD/

**Contents:**
- PETSC_VIEWER_STDOUT_WORLD#
- Level#
- Location#
- Examples#

same as PETSC_VIEWER_STDOUT_(PETSC_COMM_WORLD)

include/petscviewer.h

src/mat/tutorials/ex4.c src/mat/tutorials/ex18.c src/mat/tutorials/ex1.c src/mat/tutorials/ex11f.F90 src/mat/tutorials/ex10.c src/mat/tutorials/ex17f.F90 src/mat/tutorials/ex15.c src/mat/tutorials/ex8.c src/mat/tutorials/ex17.c src/mat/tutorials/ex4f.F90

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_VIEWER_STDOUT_
```

---

## PETSC_VIEWER_STDOUT_#

**URL:** https://petsc.org/release/manualpages/Viewer/PETSC_VIEWER_STDOUT_/

**Contents:**
- PETSC_VIEWER_STDOUT_#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a PETSCVIEWERASCII PetscViewer shared by all MPI processes in a communicator.

comm - the MPI communicator to share the PetscViewer

This object is destroyed in PetscFinalize(), PetscViewerDestroy() should never be called on it

Unlike almost all other PETSc routines, this does not return an error code. Usually used in the form

Viewers: Looking at PETSc Objects, PETSC_VIEWER_DRAW_(), PetscViewerASCIIOpen(), PETSC_VIEWER_STDERR_, PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, PetscViewerASCIIGetStdout(), PetscViewerASCIIGetStderr()

src/sys/classes/viewer/impls/ascii/vcreatea.c

Index of all Viewer routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscviewer.h"   
PetscViewer PETSC_VIEWER_STDOUT_(MPI_Comm comm)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## TSTRAJECTORYVISUALIZATION#

**URL:** https://petsc.org/release/manualpages/TS/TSTRAJECTORYVISUALIZATION/

**Contents:**
- TSTRAJECTORYVISUALIZATION#
- See Also#
- Level#
- Location#

Stores each solution of the ODE/DAE in a file for later visualization Saves each timestep into a separate file in Visualization-data/SA-%06d.bin

This version saves only the solutions at each timestep, it does not save the solution at each stage, see TSTRAJECTORYBASIC that saves all stages

\(PETSC_DIR/share/petsc/matlab/PetscReadBinaryTrajectory.m and \)PETSC_DIR/lib/petsc/bin/PetscBinaryIOTrajectory.py can read in files created with this format into MATLAB and Python.

TS: Scalable ODE and DAE Solvers, TSTrajectoryCreate(), TS, TSTrajectorySetType(), TSTrajectoryType, TSTrajectorySetVariableNames(), TSTrajectory

src/ts/trajectory/impls/visualization/trajvisualization.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Visualization-data/SA-%06d.bin
```

Example 2 (unknown):
```unknown
TSTRAJECTORYBASIC
```

Example 3 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 4 (unknown):
```unknown
TSTrajectorySetType()
```

---

## Using MATLAB with PETSc#

**URL:** https://petsc.org/release/manual/matlab/

**Contents:**
- Using MATLAB with PETSc#
- Dumping Data for MATLAB#
  - Dumping ASCII MATLAB data#
  - Dumping Binary Data for MATLAB#
- Sending Data to an Interactive MATLAB Session#
- Using the MATLAB Compute Engine#
- Licensing the MATLAB Compute Engine on a cluster#

There are three basic ways to use MATLAB with PETSc:

Dumping Data for MATLAB into files to be read into MATLAB,

Sending Data to an Interactive MATLAB Session from a running PETSc program to a MATLAB process where you may interactively type MATLAB commands (or run scripts), and

Using the MATLAB Compute Engine to send data back and forth between PETSc and MATLAB where MATLAB commands are issued, not interactively, but from a script or the PETSc program (this uses the MATLAB Engine).

For the latter two approaches one must ./configure PETSc with the argument --with-matlab [--with-matlab-dir=matlab_root_directory].

One can dump PETSc matrices and vectors to the screen in an ASCII format that MATLAB can read in directly. This is done with the command line options -vec_view ::ascii_matlab or -mat_view ::ascii_matlab. To write a file, use -vec_view :filename.m:ascii_matlab or -mat_view :filename.m:ascii_matlab.

This causes the PETSc program to print the vectors and matrices every time VecAssemblyEnd() or MatAssemblyEnd() are called. To provide finer control over when and what vectors and matrices are dumped one can use the VecView() and MatView() functions with a viewer type of PETSCVIEWERASCII (see PetscViewerASCIIOpen(), PETSC_VIEWER_STDOUT_WORLD, PETSC_VIEWER_STDOUT_SELF, or PETSC_VIEWER_STDOUT_(MPI_Comm)). Before calling the viewer set the output type with, for example,

The name of each PETSc variable printed for MATLAB may be set with

If no name is specified, the object is given a default name using PetscObjectName().

One can also read PETSc binary files (see Viewers: Looking at PETSc Objects) directly into MATLAB via the scripts available in $PETSC_DIR/share/petsc/matlab. This requires less disk space and is recommended for all but the smallest data sizes. One can also use

to dump both a PETSc binary file and a corresponding .info file which PetscReadBinaryMatlab.m will use to format the binary file in more complex cases, such as using a DMDA. For an example, see DM Tutorial ex7. In MATLAB one may then generate a useful structure. For example:

One creates a viewer to MATLAB via

(port is usually set to PETSC_DEFAULT; use NULL for the machine if the MATLAB interactive session is running on the same machine as the PETSc program) and then sends matrices or vectors via

See Viewers: Looking at PETSc Objects for more on PETSc viewers. One may start the MATLAB program manually or use the PETSc command PetscStartMatlab(MPI_Comm,char *machine,char *script,FILE **fp); where machine and script may be NULL. It is also possible to start your PETSc program from MATLAB via launch().

To receive the objects in MATLAB, make sure that $PETSC_DIR/$PETSC_ARCH/lib/petsc/matlab and $PETSC_DIR/share/petsc/matlab are in the MATLAB path. Use p = PetscOpenSocket(); (or p = PetscOpenSocket(portnum) if you provided a port number in your call to PetscViewerSocketOpen()), and then a = PetscBinaryRead(p); returns the object passed from PETSc. PetscBinaryRead() may be called any number of times. Each call should correspond on the PETSc side with viewing a single vector or matrix. close() closes the connection from MATLAB. On the PETSc side, one should destroy the viewer object with PetscViewerDestroy().

For an example, which includes sending data back to PETSc, see Vec Tutorial ex42 and the associated .m file.

One creates access to the MATLAB engine via

where machine is the name of the machine hosting MATLAB (NULL may be used for localhost). One can send objects to MATLAB via

One can get objects via

Similarly, one can send arrays via

and get them back via

One cannot use MATLAB interactively in this mode but one can send MATLAB commands via

where format has the usual printf() format. For example,

The name of each PETSc variable passed to MATLAB may be set with

Text responses can be returned from MATLAB via

There is a short-cut to starting the MATLAB engine with PETSC_MATLAB_ENGINE_(MPI_Comm).

If you are running PETSc on a cluster (or machine) that does not have a license for MATLAB, you might be able to run MATLAB on the head node of the cluster or some other machine accessible to the cluster using the -matlab_engine_host hostname option.

To activate MATLAB on head node which does not have access to the internet. [1]

First ssh into the head node using the command: ssh node_name

Obtain the Host Id using the command: ip addr | grep ether [2] You will see something like this: link/ether xx:xx:xx:xx:xx:xx ABC yy:yy:yy:yy:yy:yy Note the value: xx:xx:xx:xx:xx:xx

Login to your MathWorks Account from a computer which has internet access. You will see the available license that your account has. Select a license from the list.

Then, select Install and Activate option and select the Activate to Retrieve License File option.

Enter the information and click Continue.

An option to download the License file will appear. Download it and copy the license file to the cluster (your home directory). Now, launch MATLAB where you have sshed into your head node.

Select the Activate manually without the internet option and click Next >. Browse and locate the license file.

MATLAB is activated and ready to use.

https://www.mathworks.com/matlabcentral/answers/259627-how-do-i-activate-matlab-or-other-mathworks-products-without-an-internet-connection

http://www.mathworks.com/matlabcentral/answers/101892

Checking the PETSc version

**Examples:**

Example 1 (unknown):
```unknown
./configure
```

Example 2 (sass):
```sass
--with-matlab [--with-matlab-dir=matlab_root_directory]
```

Example 3 (julia):
```julia
-vec_view ::ascii_matlab
```

Example 4 (julia):
```julia
-mat_view ::ascii_matlab
```

---

## Viewing Objects (Viewer)#

**URL:** https://petsc.org/release/manualpages/Viewer/

**Contents:**
- Viewing Objects (Viewer)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

PETSc viewers PetscViewer print, display, and export information and data from PETSc objects in a large variety of formats.

PETSC_VIEWER_STDERR_SELF

PETSC_VIEWER_STDERR_WORLD

PETSC_VIEWER_STDOUT_SELF

PETSC_VIEWER_STDOUT_WORLD

PetscViewerASCIIGetStderr

PetscViewerASCIIGetStdout

PetscViewerASCIIOpenWithFILE

PetscViewerASCIISetFILE

PetscViewerBinaryOpen

PetscViewerBinaryRead

PetscViewerBinaryWrite

PetscViewerGLVisSetPrecision

PetscViewerGLVisSetSnapId

PetscViewerMatlabOpen

PETSC_VIEWER_BINARY_SELF

PETSC_VIEWER_BINARY_WORLD

PETSC_VIEWER_DRAW_SELF

PETSC_VIEWER_DRAW_WORLD

PETSC_VIEWER_MATLAB_SELF

PETSC_VIEWER_MATLAB_WORLD

PETSC_VIEWER_SOCKET_SELF

PETSC_VIEWER_SOCKET_WORLD

PetscOptionsCreateViewer

PetscOptionsCreateViewers

PetscOptionsHelpPrintedCheck

PetscViewerASCIIGetPointer

PetscViewerASCIIOpenWithFileUnit

PetscViewerASCIIPopSynchronized

PetscViewerASCIIPushSynchronized

PetscViewerASCIISetFileUnit

PetscViewerASCIIStdoutSetFileUnit

PetscViewerASCIISynchronizedPrintf

PetscViewerBinaryReadStringArray

PetscViewerBinaryWriteStringArray

PetscViewerCGNSGetSolutionIndex

PetscViewerCGNSGetSolutionIteration

PetscViewerCGNSGetSolutionName

PetscViewerCGNSGetSolutionTime

PetscViewerCGNSSetSolutionIndex

PetscViewerCheckReadable

PetscViewerCheckWritable

PetscViewerDrawGetBounds

PetscViewerDrawGetHold

PetscViewerDrawGetPause

PetscViewerDrawGetTitle

PetscViewerDrawResize

PetscViewerDrawSetBounds

PetscViewerDrawSetHold

PetscViewerDrawSetInfo

PetscViewerDrawSetPause

PetscViewerDrawSetTitle

PetscViewerGLVisSetFields

PetscViewerHDF5GetBaseDimension2

PetscViewerHDF5GetCollective

PetscViewerHDF5GetCompress

PetscViewerHDF5GetDefaultTimestepping

PetscViewerHDF5GetFileId

PetscViewerHDF5GetGroup

PetscViewerHDF5GetSPOutput

PetscViewerHDF5GetTimestep

PetscViewerHDF5IncrementTimestep

PetscViewerHDF5IsTimestepping

PetscViewerHDF5OpenGroup

PetscViewerHDF5PopGroup

PetscViewerHDF5PopTimestepping

PetscViewerHDF5PushGroup

PetscViewerHDF5PushTimestepping

PetscViewerHDF5SetBaseDimension2

PetscViewerHDF5SetCollective

PetscViewerHDF5SetCompress

PetscViewerHDF5SetDefaultTimestepping

PetscViewerHDF5SetSPOutput

PetscViewerHDF5SetTimestep

PetscViewerHDF5WriteGroup

PetscViewerMathematicaClearName

PetscViewerMathematicaGetName

PetscViewerMathematicaOpen

PetscViewerMathematicaSetName

PetscViewerPushFormat

PetscViewerPythonCreate

PetscViewerPythonGetType

PetscViewerPythonSetType

PetscViewerPythonViewObject

PetscViewerSetFromOptions

PetscViewerSocketOpen

PetscViewerVUFlushDeferred

PetscViewerVUGetPointer

PetscViewerVUPrintDeferred

PetscViewerViewFromOptions

PetscViewersGetViewer

PetscDataTypeToHDF5DataType

PetscHDF5DataTypeToPetscDataType

PetscViewerAppendOptionsPrefix

PetscViewerBinaryAddMPIIOOffset

PetscViewerBinaryGetDescriptor

PetscViewerBinaryGetFlowControl

PetscViewerBinaryGetInfoPointer

PetscViewerBinaryGetMPIIODescriptor

PetscViewerBinaryGetMPIIOOffset

PetscViewerBinaryGetSkipHeader

PetscViewerBinaryGetSkipInfo

PetscViewerBinaryGetSkipOptions

PetscViewerBinaryGetUseMPIIO

PetscViewerBinaryReadAll

PetscViewerBinarySetFlowControl

PetscViewerBinarySetSkipHeader

PetscViewerBinarySetSkipInfo

PetscViewerBinarySetSkipOptions

PetscViewerBinarySetUseMPIIO

PetscViewerBinarySkipInfo

PetscViewerBinaryWriteAll

PetscViewerFileGetMode

PetscViewerFileGetName

PetscViewerFileSetMode

PetscViewerFileSetName

PetscViewerGetOptionsPrefix

PetscViewerGetSubViewer

PetscViewerHDF5HasAttribute

PetscViewerHDF5HasDataset

PetscViewerHDF5HasGroup

PetscViewerHDF5HasObject

PetscViewerHDF5HasObjectAttribute

PetscViewerHDF5ReadAttribute

PetscViewerHDF5ReadObjectAttribute

PetscViewerHDF5ReadSizes

PetscViewerHDF5WriteAttribute

PetscViewerHDF5WriteObjectAttribute

PetscViewerMathematicaSkipPackets

PetscViewerMatlabGetArray

PetscViewerMatlabPutArray

PetscViewerMatlabPutVariable

PetscViewerRestoreSubViewer

PetscViewerSetOptionsPrefix

PetscViewerSocketSetConnection

PetscViewerStringGetStringRead

PetscViewerStringOpen

PetscViewerStringSetOwnString

PetscViewerStringSetString

PetscViewerVUGetVecSeen

PETSC_VIEWER_PYVISTA_

PetscOptionsGetCreateViewerOff

PetscOptionsHelpPrintedCreate

PetscOptionsHelpPrintedDestroy

PetscOptionsPopCreateViewerOff

PetscOptionsPushCreateViewerOff

PetscSysFinalizePackage

PetscSysInitializePackage

PetscViewerASCIIAddTab

PetscViewerASCIIGetTab

PetscViewerASCIIPopTab

PetscViewerASCIIPrintf

PetscViewerASCIIPushTab

PetscViewerASCIISetTab

PetscViewerASCIISubtractTab

PetscViewerASCIIUseTabs

PetscViewerAndFormatCreate

PetscViewerAndFormatDestroy

PetscViewerDrawBaseAdd

PetscViewerDrawBaseSet

PetscViewerFinalizePackage

PetscViewerFlowControlEndMain

PetscViewerFlowControlEndWorker

PetscViewerFlowControlStart

PetscViewerFlowControlStepMain

PetscViewerFlowControlStepWorker

PetscViewerHDF5PathIsRelative

PetscViewerInitializePackage

PetscViewerMathematicaFinalizePackage

PetscViewerMathematicaInitializePackage

PetscViewerMathematicaPutCSRMatrix

PetscViewerMathematicaPutMatrix

PetscViewerMonitorLGSetUp

PetscViewerRegisterAll

PetscViewerStringSPrintf

PetscViewerVTKAddField

PetscViewerVTKFieldType

PetscViewerVTKWriteFunction

PetscViewerVUSetVecSeen

PETSC_VIEWER_BINARY_SELF

PETSC_VIEWER_BINARY_WORLD

PETSC_VIEWER_DRAW_SELF

PETSC_VIEWER_DRAW_WORLD

PETSC_VIEWER_MATLAB_SELF

PETSC_VIEWER_MATLAB_WORLD

PETSC_VIEWER_PYVISTA_

PETSC_VIEWER_SOCKET_SELF

PETSC_VIEWER_SOCKET_WORLD

PETSC_VIEWER_STDERR_SELF

PETSC_VIEWER_STDERR_WORLD

PETSC_VIEWER_STDOUT_SELF

PETSC_VIEWER_STDOUT_WORLD

PetscDataTypeToHDF5DataType

PetscHDF5DataTypeToPetscDataType

PetscOptionsCreateViewer

PetscOptionsCreateViewers

PetscOptionsGetCreateViewerOff

PetscOptionsHelpPrintedCheck

PetscOptionsHelpPrintedCreate

PetscOptionsHelpPrintedDestroy

PetscOptionsPopCreateViewerOff

PetscOptionsPushCreateViewerOff

PetscSysFinalizePackage

PetscSysInitializePackage

PetscViewerASCIIAddTab

PetscViewerASCIIGetPointer

PetscViewerASCIIGetStderr

PetscViewerASCIIGetStdout

PetscViewerASCIIGetTab

PetscViewerASCIIOpenWithFILE

PetscViewerASCIIOpenWithFileUnit

PetscViewerASCIIPopSynchronized

PetscViewerASCIIPopTab

PetscViewerASCIIPrintf

PetscViewerASCIIPushSynchronized

PetscViewerASCIIPushTab

PetscViewerASCIISetFILE

PetscViewerASCIISetFileUnit

PetscViewerASCIISetTab

PetscViewerASCIIStdoutSetFileUnit

PetscViewerASCIISubtractTab

PetscViewerASCIISynchronizedPrintf

PetscViewerASCIIUseTabs

PetscViewerAndFormatCreate

PetscViewerAndFormatDestroy

PetscViewerAppendOptionsPrefix

PetscViewerBinaryAddMPIIOOffset

PetscViewerBinaryGetDescriptor

PetscViewerBinaryGetFlowControl

PetscViewerBinaryGetInfoPointer

PetscViewerBinaryGetMPIIODescriptor

PetscViewerBinaryGetMPIIOOffset

PetscViewerBinaryGetSkipHeader

PetscViewerBinaryGetSkipInfo

PetscViewerBinaryGetSkipOptions

PetscViewerBinaryGetUseMPIIO

PetscViewerBinaryOpen

PetscViewerBinaryRead

PetscViewerBinaryReadAll

PetscViewerBinaryReadStringArray

PetscViewerBinarySetFlowControl

PetscViewerBinarySetSkipHeader

PetscViewerBinarySetSkipInfo

PetscViewerBinarySetSkipOptions

PetscViewerBinarySetUseMPIIO

PetscViewerBinarySkipInfo

PetscViewerBinaryWrite

PetscViewerBinaryWriteAll

PetscViewerBinaryWriteStringArray

PetscViewerCGNSGetSolutionIndex

PetscViewerCGNSGetSolutionIteration

PetscViewerCGNSGetSolutionName

PetscViewerCGNSGetSolutionTime

PetscViewerCGNSSetSolutionIndex

PetscViewerCheckReadable

PetscViewerCheckWritable

PetscViewerDrawBaseAdd

PetscViewerDrawBaseSet

PetscViewerDrawGetBounds

PetscViewerDrawGetHold

PetscViewerDrawGetPause

PetscViewerDrawGetTitle

PetscViewerDrawResize

PetscViewerDrawSetBounds

PetscViewerDrawSetHold

PetscViewerDrawSetInfo

PetscViewerDrawSetPause

PetscViewerDrawSetTitle

PetscViewerFileGetMode

PetscViewerFileGetName

PetscViewerFileSetMode

PetscViewerFileSetName

PetscViewerFinalizePackage

PetscViewerFlowControlEndMain

PetscViewerFlowControlEndWorker

PetscViewerFlowControlStart

PetscViewerFlowControlStepMain

PetscViewerFlowControlStepWorker

PetscViewerGLVisSetFields

PetscViewerGLVisSetPrecision

PetscViewerGLVisSetSnapId

PetscViewerGetOptionsPrefix

PetscViewerGetSubViewer

PetscViewerHDF5GetBaseDimension2

PetscViewerHDF5GetCollective

PetscViewerHDF5GetCompress

PetscViewerHDF5GetDefaultTimestepping

PetscViewerHDF5GetFileId

PetscViewerHDF5GetGroup

PetscViewerHDF5GetSPOutput

PetscViewerHDF5GetTimestep

PetscViewerHDF5HasAttribute

PetscViewerHDF5HasDataset

PetscViewerHDF5HasGroup

PetscViewerHDF5HasObject

PetscViewerHDF5HasObjectAttribute

PetscViewerHDF5IncrementTimestep

PetscViewerHDF5IsTimestepping

PetscViewerHDF5OpenGroup

PetscViewerHDF5PathIsRelative

PetscViewerHDF5PopGroup

PetscViewerHDF5PopTimestepping

PetscViewerHDF5PushGroup

PetscViewerHDF5PushTimestepping

PetscViewerHDF5ReadAttribute

PetscViewerHDF5ReadObjectAttribute

PetscViewerHDF5ReadSizes

PetscViewerHDF5SetBaseDimension2

PetscViewerHDF5SetCollective

PetscViewerHDF5SetCompress

PetscViewerHDF5SetDefaultTimestepping

PetscViewerHDF5SetSPOutput

PetscViewerHDF5SetTimestep

PetscViewerHDF5WriteAttribute

PetscViewerHDF5WriteGroup

PetscViewerHDF5WriteObjectAttribute

PetscViewerInitializePackage

PetscViewerMathematicaClearName

PetscViewerMathematicaFinalizePackage

PetscViewerMathematicaGetName

PetscViewerMathematicaInitializePackage

PetscViewerMathematicaOpen

PetscViewerMathematicaPutCSRMatrix

PetscViewerMathematicaPutMatrix

PetscViewerMathematicaSetName

PetscViewerMathematicaSkipPackets

PetscViewerMatlabGetArray

PetscViewerMatlabOpen

PetscViewerMatlabPutArray

PetscViewerMatlabPutVariable

PetscViewerMonitorLGSetUp

PetscViewerPushFormat

PetscViewerPythonCreate

PetscViewerPythonGetType

PetscViewerPythonSetType

PetscViewerPythonViewObject

PetscViewerRegisterAll

PetscViewerRestoreSubViewer

PetscViewerSetFromOptions

PetscViewerSetOptionsPrefix

PetscViewerSocketOpen

PetscViewerSocketSetConnection

PetscViewerStringGetStringRead

PetscViewerStringOpen

PetscViewerStringSPrintf

PetscViewerStringSetOwnString

PetscViewerStringSetString

PetscViewerVTKAddField

PetscViewerVTKFieldType

PetscViewerVTKWriteFunction

PetscViewerVUFlushDeferred

PetscViewerVUGetPointer

PetscViewerVUGetVecSeen

PetscViewerVUPrintDeferred

PetscViewerVUSetVecSeen

PetscViewerViewFromOptions

PetscViewersGetViewer

System Routines, Profiling, Data Structures

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

---
