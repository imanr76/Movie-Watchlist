from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Movie:
    _id : str
    title : str
    director : str
    year : int
    rating : int = 0
    cast : list[str] = field(default_factory=list)
    series : list[str] = field(default_factory=list)
    description : list[str] = field(default_factory=list)
    tags : list[str] = field(default_factory=list)
    video_link : str = None
    last_watched : datetime = None
    
    